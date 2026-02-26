from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Exercise, TestCase, Hint, Concept, UserProgress, Level
from schemas import ExerciseDetail, HintResponse
from security import get_current_user
from models import User

router = APIRouter()


@router.get("/{exercise_id}", response_model=ExerciseDetail)
def get_exercise(
    exercise_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ex = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not ex:
        raise HTTPException(status_code=404, detail="Exercise not found")

    level = db.query(Level).filter(Level.id == ex.level_id).first()
    if current_user.total_xp < level.unlock_xp_required:
        raise HTTPException(status_code=403, detail="Level not unlocked")

    progress = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.exercise_id == exercise_id,
    ).first()

    attempt_count = progress.attempt_count if progress else 0

    # Only return hints user has unlocked based on attempt count
    hints = db.query(Hint).filter(
        Hint.exercise_id == exercise_id,
        Hint.unlock_after_attempts <= attempt_count,
    ).order_by(Hint.order_num).all()

    # Concepts unlock after failures
    concepts = []
    if progress and progress.failed_attempts >= 3:
        concepts = db.query(Concept).filter(Concept.exercise_id == exercise_id).all()

    # Only non-hidden test cases visible to user
    visible_tests = db.query(TestCase).filter(
        TestCase.exercise_id == exercise_id,
        TestCase.is_hidden == False,
    ).all()

    # Calculate next_exercise_id
    next_ex = db.query(Exercise).filter(
        Exercise.level_id == ex.level_id,
        Exercise.order_in_level > ex.order_in_level
    ).order_by(Exercise.order_in_level.asc()).first()
    
    if not next_ex:
        next_level = db.query(Level).filter(Level.level_number > level.level_number).order_by(Level.level_number.asc()).first()
        if next_level:
            next_ex = db.query(Exercise).filter(Exercise.level_id == next_level.id).order_by(Exercise.order_in_level.asc()).first()
            
    next_exercise_id = next_ex.id if next_ex else None

    return {
        "id": ex.id,
        "title": ex.title,
        "problem_statement": ex.problem_statement,
        "scenario": ex.scenario,
        "input_description": ex.input_description,
        "expected_output_description": ex.expected_output_description,
        "starter_code": ex.starter_code,
        "tags": ex.tags,
        "difficulty": ex.difficulty,
        "xp_reward": ex.xp_reward,
        "allowed_imports": ex.allowed_imports,
        "timeout_secs": ex.timeout_secs,
        "order_in_level": ex.order_in_level,
        "is_completed": progress.completed if progress else False,
        "attempt_count": attempt_count,
        "visible_test_cases": [
            {"input_data": t.input_data, "expected_output": t.expected_output}
            for t in visible_tests
        ],
        "unlocked_hints": hints,
        "concepts": concepts,
        "next_exercise_id": next_exercise_id,
    }
