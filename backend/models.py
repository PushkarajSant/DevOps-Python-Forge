from sqlalchemy import Column, Integer, String, Text, Boolean, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    full_name = Column(String(100), nullable=True)
    role = Column(String(20), default="user")  # user | admin
    total_xp = Column(Integer, default=0)
    current_level = Column(Integer, default=0)
    streak_days = Column(Integer, default=0)
    last_active_date = Column(String(20), nullable=True)
    total_submissions = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    submissions = relationship("Submission", back_populates="user")
    achievements = relationship("Achievement", back_populates="user")
    progress = relationship("UserProgress", back_populates="user")


class Level(Base):
    __tablename__ = "levels"
    id = Column(Integer, primary_key=True, index=True)
    level_number = Column(Integer, unique=True, nullable=False, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    color = Column(String(20), default="#22c55e")
    unlock_xp_required = Column(Integer, default=0)
    min_exercises_to_pass = Column(Integer, default=5)
    exercises = relationship("Exercise", back_populates="level")
    user_progress = relationship("UserProgress", back_populates="level")


class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(Integer, primary_key=True, index=True)
    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)
    title = Column(String(200), nullable=False)
    problem_statement = Column(Text, nullable=False)
    scenario = Column(Text, nullable=False)
    input_description = Column(Text, nullable=False)
    expected_output_description = Column(Text, nullable=False)
    starter_code = Column(Text, default="")
    tags = Column(JSON, default=[])
    difficulty = Column(String(20), default="easy")  # easy | medium | hard
    order_in_level = Column(Integer, default=0)
    xp_reward = Column(Integer, default=10)
    allowed_imports = Column(JSON, default=[])
    timeout_secs = Column(Integer, default=5)
    requires_function = Column(String(100), nullable=True)
    is_capstone = Column(Boolean, default=False)
    level = relationship("Level", back_populates="exercises")
    test_cases = relationship("TestCase", back_populates="exercise")
    hints = relationship("Hint", back_populates="exercise", order_by="Hint.order_num")
    concepts = relationship("Concept", back_populates="exercise")
    submissions = relationship("Submission", back_populates="exercise")
    progress = relationship("UserProgress", back_populates="exercise")


class TestCase(Base):
    __tablename__ = "test_cases"
    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    input_data = Column(Text, default="")
    expected_output = Column(Text, nullable=False)
    is_hidden = Column(Boolean, default=True)
    comparison_mode = Column(String(20), default="exact")  # exact | json | contains | regex
    exercise = relationship("Exercise", back_populates="test_cases")


class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    code = Column(Text, nullable=False)
    stdout = Column(Text, default="")
    stderr = Column(Text, default="")
    passed = Column(Boolean, default=False)
    execution_time_ms = Column(Float, default=0)
    xp_awarded = Column(Integer, default=0)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="submissions")
    exercise = relationship("Exercise", back_populates="submissions")


class Hint(Base):
    __tablename__ = "hints"
    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    order_num = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    unlock_after_attempts = Column(Integer, default=1)
    exercise = relationship("Exercise", back_populates="hints")


class Concept(Base):
    __tablename__ = "concepts"
    id = Column(Integer, primary_key=True, index=True)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    title = Column(String(200), nullable=False)
    explanation = Column(Text, nullable=False)
    code_example = Column(Text, default="")
    unlocks_after_failures = Column(Integer, default=3)
    exercise = relationship("Exercise", back_populates="concepts")


class Achievement(Base):
    __tablename__ = "achievements"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    badge_type = Column(String(50), nullable=False)
    badge_name = Column(String(100), nullable=False)
    description = Column(Text, default="")
    earned_at = Column(DateTime(timezone=True), server_default=func.now())
    user = relationship("User", back_populates="achievements")


class UserProgress(Base):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)
    completed = Column(Boolean, default=False)
    attempt_count = Column(Integer, default=0)
    failed_attempts = Column(Integer, default=0)
    last_attempted_at = Column(DateTime(timezone=True), nullable=True)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    user = relationship("User", back_populates="progress")
    exercise = relationship("Exercise", back_populates="progress")
    level = relationship("Level", back_populates="user_progress")
