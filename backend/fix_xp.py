import sys
import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Set up DB connection natively
engine = create_engine("sqlite:///devops_forge.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def fix_level_1_xp():
    db = SessionLocal()
    try:
        db.execute(text("UPDATE levels SET unlock_xp_required = 40 WHERE level_number = 1"))
        db.commit()
        print("Successfully updated Level 1 unlock_xp_required to 40 XP!")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    fix_level_1_xp()
