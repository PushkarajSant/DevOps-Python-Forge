"""
Admin router — exercise CRUD, test case management, and platform stats.
Requires admin role.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

from database import get_db
from models import User, Exercise, Level, TestCase, Submission, Hint, Concept, UserProgress
from schemas import ExerciseCreate, ExerciseUpdate, TestCaseCreate, AdminStats
from security import require_admin

router = APIRouter()


# ──────────────────────────────────────────────────────────────────────────────
# Dashboard Stats
# ──────────────────────────────────────────────────────────────────────────────

@router.get("/stats", response_model=AdminStats)
def get_admin_stats(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    """Platform-wide statistics."""
    total_users = db.query(User).count()
    total_submissions = db.query(Submission).count()
    total_exercises = db.query(Exercise).count()
    total_levels = db.query(Level).count()

    total_passed = db.query(Submission).filter(Submission.passed == True).count()
    avg_pass_rate = (total_passed / total_submissions * 100) if total_submissions > 0 else 0.0

    return AdminStats(
        total_users=total_users,
        total_submissions=total_submissions,
        total_exercises=total_exercises,
        total_levels=total_levels,
        avg_pass_rate=round(avg_pass_rate, 1),
    )


# ──────────────────────────────────────────────────────────────────────────────
# Exercise CRUD
# ──────────────────────────────────────────────────────────────────────────────

@router.get("/exercises")
def list_all_exercises(
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
    level_id: int = None,
):
    """List all exercises, optionally filtered by level."""
    q = db.query(Exercise)
    if level_id:
        q = q.filter(Exercise.level_id == level_id)
    exercises = q.order_by(Exercise.level_id, Exercise.order_in_level).all()
    return [
        {
            "id": e.id,
            "title": e.title,
            "level_id": e.level_id,
            "difficulty": e.difficulty,
            "xp_reward": e.xp_reward,
            "order_in_level": e.order_in_level,
            "test_case_count": len(e.test_cases),
            "submission_count": db.query(Submission).filter(Submission.exercise_id == e.id).count(),
        }
        for e in exercises
    ]


@router.post("/exercises")
def create_exercise(
    data: ExerciseCreate,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Create a new exercise."""
    level = db.query(Level).filter(Level.id == data.level_id).first()
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")

    exercise = Exercise(
        level_id=data.level_id,
        title=data.title,
        problem_statement=data.problem_statement,
        scenario=data.scenario,
        input_description=data.input_description,
        expected_output_description=data.expected_output_description,
        starter_code=data.starter_code,
        tags=data.tags,
        difficulty=data.difficulty,
        xp_reward=data.xp_reward,
        allowed_imports=data.allowed_imports,
        timeout_secs=data.timeout_secs,
        order_in_level=data.order_in_level,
    )
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return {"id": exercise.id, "title": exercise.title, "created": True}


@router.put("/exercises/{exercise_id}")
def update_exercise(
    exercise_id: int,
    data: ExerciseUpdate,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Update an existing exercise."""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            setattr(exercise, key, value)

    db.commit()
    db.refresh(exercise)
    return {"id": exercise.id, "title": exercise.title, "updated": True}


@router.delete("/exercises/{exercise_id}")
def delete_exercise(
    exercise_id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Delete an exercise and its related data."""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    db.query(TestCase).filter(TestCase.exercise_id == exercise_id).delete()
    db.query(Hint).filter(Hint.exercise_id == exercise_id).delete()
    db.query(Concept).filter(Concept.exercise_id == exercise_id).delete()
    db.query(Submission).filter(Submission.exercise_id == exercise_id).delete()
    db.query(UserProgress).filter(UserProgress.exercise_id == exercise_id).delete()
    db.delete(exercise)
    db.commit()
    return {"deleted": True}


# ──────────────────────────────────────────────────────────────────────────────
# Test Case Management
# ──────────────────────────────────────────────────────────────────────────────

@router.post("/test-cases")
def create_test_case(
    data: TestCaseCreate,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Add a test case to an exercise."""
    exercise = db.query(Exercise).filter(Exercise.id == data.exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    tc = TestCase(
        exercise_id=data.exercise_id,
        input_data=data.input_data,
        expected_output=data.expected_output,
        is_hidden=data.is_hidden,
        comparison_mode=data.comparison_mode,
        order_num=data.order_num,
    )
    db.add(tc)
    db.commit()
    db.refresh(tc)
    return {"id": tc.id, "created": True}


@router.delete("/test-cases/{tc_id}")
def delete_test_case(
    tc_id: int,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Delete a test case."""
    tc = db.query(TestCase).filter(TestCase.id == tc_id).first()
    if not tc:
        raise HTTPException(status_code=404, detail="Test case not found")
    db.delete(tc)
    db.commit()
    return {"deleted": True}


# ──────────────────────────────────────────────────────────────────────────────
# User Management
# ──────────────────────────────────────────────────────────────────────────────

@router.get("/users")
def list_users(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    """List all users with stats."""
    users = db.query(User).order_by(User.created_at.desc()).all()
    return [
        {
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role,
            "total_xp": u.total_xp,
            "current_level": u.current_level,
            "total_submissions": u.total_submissions,
            "created_at": u.created_at,
        }
        for u in users
    ]


@router.put("/users/{user_id}/role")
def update_user_role(
    user_id: int,
    role: str,
    admin: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """Promote/demote a user."""
    if role not in ("user", "admin"):
        raise HTTPException(status_code=400, detail="Role must be 'user' or 'admin'")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role = role
    db.commit()
    return {"id": user.id, "username": user.username, "role": user.role}
