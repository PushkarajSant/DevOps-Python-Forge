from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import UserProgress, Level, Exercise, User, Submission
from security import get_current_user

router = APIRouter()


@router.get("")
def get_global_progress(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Returns global progress for the tracks."""
    total_exercises = db.query(Exercise).count()
    completed_exercises = db.query(UserProgress).filter(
        UserProgress.user_id == current_user.id,
        UserProgress.completed == True
    ).count()
    
    return {
        "total_exercises": total_exercises,
        "completed": completed_exercises
    }

@router.get("/dashboard")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    levels = db.query(Level).order_by(Level.level_number).all()
    level_progress = []
    for level in levels:
        total = db.query(Exercise).filter(Exercise.level_id == level.id).count()
        completed = db.query(UserProgress).filter(
            UserProgress.user_id == current_user.id,
            UserProgress.level_id == level.id,
            UserProgress.completed == True,
        ).count()
        level_progress.append({
            "level_number": level.level_number,
            "title": level.title,
            "color": level.color,
            "total": total,
            "completed": completed,
            "percentage": round((completed / total * 100) if total else 0, 1),
            "is_unlocked": current_user.total_xp >= level.unlock_xp_required,
        })

    recent_submissions = db.query(Submission).filter(
        Submission.user_id == current_user.id,
    ).order_by(Submission.submitted_at.desc()).limit(5).all()

    return {
        "user": {
            "username": current_user.username,
            "full_name": current_user.full_name,
            "total_xp": current_user.total_xp,
            "current_level": current_user.current_level,
            "streak_days": current_user.streak_days,
        },
        "level_progress": level_progress,
        "recent_submissions": [
            {
                "id": s.id,
                "exercise_id": s.exercise_id,
                "passed": s.passed,
                "xp_awarded": s.xp_awarded,
                "submitted_at": s.submitted_at,
            }
            for s in recent_submissions
        ],
    }
