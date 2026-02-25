from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models import Exercise, Submission, UserProgress, TestCase, Level, User
from schemas import SubmissionCreate, SubmissionResponse
from security import get_current_user
from execution.runner import run_code, validate_output

router = APIRouter()


@router.post("/{exercise_id}/run")
def run_exercise(
    exercise_id: int,
    body: SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Run code without submitting — test mode."""
    ex = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not ex:
        raise HTTPException(status_code=404, detail="Exercise not found")

    result = run_code(
        code=body.code,
        input_data=body.custom_input or "",
        allowed_imports=ex.allowed_imports or [],
        timeout_secs=ex.timeout_secs,
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "execution_time_ms": result.execution_time_ms,
        "timed_out": result.timed_out,
        "error": result.error,
    }


@router.post("/{exercise_id}/submit", response_model=SubmissionResponse)
def submit_exercise(
    exercise_id: int,
    body: SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ex = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not ex:
        raise HTTPException(status_code=404, detail="Exercise not found")

    level = db.query(Level).filter(Level.id == ex.level_id).first()
    if current_user.total_xp < level.unlock_xp_required:
        raise HTTPException(status_code=403, detail="Level not unlocked")

    test_cases = db.query(TestCase).filter(TestCase.exercise_id == exercise_id).all()

    all_passed = True
    test_results = []
    total_time = 0

    for tc in test_cases:
        result = run_code(
            code=body.code,
            input_data=tc.input_data,
            allowed_imports=ex.allowed_imports or [],
            timeout_secs=ex.timeout_secs,
        )
        total_time += result.execution_time_ms

        if result.error or result.timed_out:
            passed = False
            feedback = result.error or "Time limit exceeded"
        else:
            passed, feedback = validate_output(
                actual=result.stdout,
                expected=tc.expected_output,
                mode=tc.comparison_mode,
            )

        if not passed:
            all_passed = False

        test_results.append({
            "test_case_id": tc.id,
            "is_hidden": tc.is_hidden,
            "passed": passed,
            "feedback": None if tc.is_hidden else feedback,
            "execution_time_ms": result.execution_time_ms,
        })

    # Update or create UserProgress
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.exercise_id == exercise_id,
    ).first()

    if not progress:
        progress = UserProgress(
            user_id=current_user.id,
            exercise_id=exercise_id,
            level_id=ex.level_id,
            attempt_count=0,
            failed_attempts=0,
            completed=False,
        )
        db.add(progress)

    progress.attempt_count += 1
    progress.last_attempted_at = datetime.utcnow()

    xp_awarded = 0
    if all_passed and not progress.completed:
        progress.completed = True
        progress.completed_at = datetime.utcnow()
        xp_awarded = ex.xp_reward
        current_user.total_xp = (current_user.total_xp or 0) + xp_awarded
        # Update user level
        level_number = level.level_number
        if level_number > (current_user.current_level or 0):
            current_user.current_level = level_number
    elif not all_passed:
        progress.failed_attempts = (progress.failed_attempts or 0) + 1

    # Save submission record
    submission = Submission(
        user_id=current_user.id,
        exercise_id=exercise_id,
        code=body.code,
        passed=all_passed,
        execution_time_ms=total_time,
        xp_awarded=xp_awarded,
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)

    # Build smart failure feedback
    failure_message = None
    if not all_passed:
        failure_message = _build_failure_feedback(body.code, test_results)

    return {
        "id": submission.id,
        "passed": all_passed,
        "test_results": test_results,
        "xp_awarded": xp_awarded,
        "total_xp": current_user.total_xp,
        "execution_time_ms": total_time,
        "attempt_count": progress.attempt_count,
        "failure_message": failure_message,
        "hints_unlocked": progress.attempt_count,
    }


def _build_failure_feedback(code: str, test_results: list) -> str:
    """Generate conceptual feedback without revealing solutions."""
    import ast
    feedback_parts = []

    # Check for missing return
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                has_return = any(isinstance(n, ast.Return) for n in ast.walk(node))
                if not has_return:
                    feedback_parts.append(
                        f"⚠ Your function '{node.name}' doesn't return a value. "
                        "Use `return` to produce output from functions."
                    )
    except SyntaxError as e:
        return f"❌ Syntax Error: {e}"

    # Check for common output issues
    failed_visible = [r for r in test_results if not r["passed"] and not r["is_hidden"]]
    if failed_visible and failed_visible[0].get("feedback"):
        feedback_parts.append(f"💡 {failed_visible[0]['feedback']}")

    return "\n".join(feedback_parts) or "Check your output format and logic carefully."
