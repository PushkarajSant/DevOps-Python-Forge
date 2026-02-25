from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Level, Exercise, UserProgress
from schemas import LevelResponse, ExerciseListItem
from security import get_current_user
from models import User

router = APIRouter()


@router.get("/", response_model=List[LevelResponse])
def get_levels(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    levels = db.query(Level).order_by(Level.level_number).all()
    result = []
    for level in levels:
        exercise_count = db.query(Exercise).filter(Exercise.level_id == level.id).count()
        completed_count = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.level_id == level.id,
            UserProgress.completed == True,
        ).count()
        is_unlocked = current_user.total_xp >= level.unlock_xp_required
        result.append({
            "id": level.id,
            "level_number": level.level_number,
            "title": level.title,
            "description": level.description,
            "color": level.color,
            "unlock_xp_required": level.unlock_xp_required,
            "min_exercises_to_pass": level.min_exercises_to_pass,
            "exercise_count": exercise_count,
            "completed_count": completed_count,
            "is_unlocked": is_unlocked,
        })
    return result


@router.get("/{level_number}/exercises", response_model=List[ExerciseListItem])
def get_level_exercises(
    level_number: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    level = db.query(Level).filter(Level.level_number == level_number).first()
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")
    if current_user.total_xp < level.unlock_xp_required:
        raise HTTPException(status_code=403, detail="Level not unlocked yet")
    exercises = db.query(Exercise).filter(
        Exercise.level_id == level.id
    ).order_by(Exercise.order_in_level).all()
    result = []
    for ex in exercises:
        progress = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.exercise_id == ex.id,
        ).first()
        result.append({
            "id": ex.id,
            "title": ex.title,
            "difficulty": ex.difficulty,
            "xp_reward": ex.xp_reward,
            "tags": ex.tags,
            "order_in_level": ex.order_in_level,
            "is_completed": progress.completed if progress else False,
            "attempts": progress.attempt_count if progress else 0,
        })
    return result
