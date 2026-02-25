from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserResponse
from security import get_current_user

router = APIRouter()


@router.get("/me", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/leaderboard")
def get_leaderboard(db: Session = Depends(get_db)):
    top_users = db.query(User).order_by(User.total_xp.desc()).limit(20).all()
    return [
        {
            "rank": i + 1,
            "username": u.username,
            "full_name": u.full_name,
            "total_xp": u.total_xp,
            "current_level": u.current_level,
            "streak_days": u.streak_days,
        }
        for i, u in enumerate(top_users)
    ]
