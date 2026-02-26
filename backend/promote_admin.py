import sys
import os

# Add the backend directory to sys.path so we can import from the database package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import User

def promote_to_admin(username=None):
    db = SessionLocal()
    try:
        if username:
            user = db.query(User).filter(User.username == username).first()
        else:
            user = db.query(User).first()
            
        if user:
            user.role = 'admin'
            db.commit()
            print(f'Successfully promoted user "{user.username}" to admin role!')
        else:
            print(f'User "{username}" not found.' if username else "No users found in database.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        promote_to_admin(sys.argv[1])
    else:
        promote_to_admin()
