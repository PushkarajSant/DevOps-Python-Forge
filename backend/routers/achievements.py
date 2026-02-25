"""
Achievements router — badge management and auto-awarding logic.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Achievement, User, Submission, UserProgress, Level
from schemas import AchievementResponse
from security import get_current_user

router = APIRouter()

# ──────────────────────────────────────────────────────────────────────────────
# Badge definitions — (badge_type, badge_name, description, check_function)
# ──────────────────────────────────────────────────────────────────────────────

BADGE_DEFINITIONS = {
    "first_solve": {
        "name": "🔥 First Blood",
        "description": "Solve your first exercise",
    },
    "streak_3": {
        "name": "⚡ Hot Streak",
        "description": "Maintain a 3-day coding streak",
    },
    "streak_7": {
        "name": "🔥 Week Warrior",
        "description": "Maintain a 7-day coding streak",
    },
    "streak_30": {
        "name": "💎 Monthly Master",
        "description": "Maintain a 30-day coding streak",
    },
    "level_1": {
        "name": "🚀 Liftoff",
        "description": "Complete Level 0 and unlock Level 1",
    },
    "level_5": {
        "name": "⭐ Halfway Hero",
        "description": "Reach Level 5",
    },
    "level_10": {
        "name": "🏆 Forge Master",
        "description": "Reach Level 10 — Capstone Projects",
    },
    "xp_100": {
        "name": "📊 Centennial",
        "description": "Earn 100 XP total",
    },
    "xp_500": {
        "name": "🎯 High Achiever",
        "description": "Earn 500 XP total",
    },
    "xp_1000": {
        "name": "👑 XP King",
        "description": "Earn 1000 XP total",
    },
    "perfect_level": {
        "name": "💯 Perfectionist",
        "description": "Complete all exercises in a level",
    },
    "first_try": {
        "name": "🎯 Bullseye",
        "description": "Solve an exercise on the first attempt",
    },
    "fifty_solves": {
        "name": "🏅 50 & Counting",
        "description": "Solve 50 exercises",
    },
    "hundred_solves": {
        "name": "🌟 Centurion",
        "description": "Solve 100 exercises",
    },
    "night_owl": {
        "name": "🦉 Night Owl",
        "description": "Submit a solution between midnight and 5 AM",
    },
    "speed_demon": {
        "name": "⚡ Speed Demon",
        "description": "Solve an exercise in under 30 seconds",
    },
}


@router.get("/", response_model=List[AchievementResponse])
def get_achievements(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all achievements for the current user."""
    return db.query(Achievement).filter(Achievement.user_id == current_user.id).order_by(Achievement.earned_at.desc()).all()


@router.get("/available")
def get_available_badges(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """List all badges with earned status."""
    earned = {a.badge_type for a in db.query(Achievement).filter(Achievement.user_id == current_user.id).all()}
    result = []
    for badge_type, info in BADGE_DEFINITIONS.items():
        result.append({
            "badge_type": badge_type,
            "badge_name": info["name"],
            "description": info["description"],
            "earned": badge_type in earned,
        })
    return result


def check_and_award_badges(user: User, db: Session) -> List[dict]:
    """
    Check all badge conditions and award any newly earned badges.
    Called after each successful submission.
    Returns list of newly awarded badges.
    """
    earned = {a.badge_type for a in db.query(Achievement).filter(Achievement.user_id == user.id).all()}
    new_badges = []

    # Count completed exercises
    completed_count = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.completed == True,
    ).count()

    checks = [
        ("first_solve", completed_count >= 1),
        ("fifty_solves", completed_count >= 50),
        ("hundred_solves", completed_count >= 100),
        ("streak_3", user.streak_days >= 3),
        ("streak_7", user.streak_days >= 7),
        ("streak_30", user.streak_days >= 30),
        ("level_1", user.current_level >= 1),
        ("level_5", user.current_level >= 5),
        ("level_10", user.current_level >= 10),
        ("xp_100", user.total_xp >= 100),
        ("xp_500", user.total_xp >= 500),
        ("xp_1000", user.total_xp >= 1000),
    ]

    # Check for perfect level (all exercises in any level completed)
    levels = db.query(Level).all()
    for level in levels:
        total = len(level.exercises)
        if total > 0:
            completed_in_level = db.query(UserProgress).filter(
                UserProgress.user_id == user.id,
                UserProgress.level_id == level.id,
                UserProgress.completed == True,
            ).count()
            if completed_in_level == total:
                checks.append(("perfect_level", True))
                break

    for badge_type, condition in checks:
        if badge_type not in earned and condition:
            info = BADGE_DEFINITIONS.get(badge_type, {})
            achievement = Achievement(
                user_id=user.id,
                badge_type=badge_type,
                badge_name=info.get("name", badge_type),
                description=info.get("description", ""),
            )
            db.add(achievement)
            new_badges.append({
                "badge_type": badge_type,
                "badge_name": info.get("name", badge_type),
                "description": info.get("description", ""),
            })

    if new_badges:
        db.commit()

    return new_badges
