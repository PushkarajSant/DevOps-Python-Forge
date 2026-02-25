from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel, EmailStr


# ─── Auth ─────────────────────────────────────────────────────────────────────
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str]
    role: str
    total_xp: int
    current_level: int
    streak_days: int
    total_submissions: int
    created_at: datetime

    class Config:
        from_attributes = True


# ─── Levels ───────────────────────────────────────────────────────────────────
class LevelResponse(BaseModel):
    id: int
    level_number: int
    title: str
    description: str
    color: str
    unlock_xp_required: int
    min_exercises_to_pass: int
    exercise_count: int
    completed_count: int
    is_unlocked: bool

    class Config:
        from_attributes = True


# ─── Exercises ────────────────────────────────────────────────────────────────
class ExerciseListItem(BaseModel):
    id: int
    title: str
    difficulty: str
    xp_reward: int
    tags: List[str]
    order_in_level: int
    is_completed: bool
    attempts: int

    class Config:
        from_attributes = True


class VisibleTestCase(BaseModel):
    input_data: str
    expected_output: str


class HintResponse(BaseModel):
    id: int
    order_num: int
    content: str
    unlock_after_attempts: int

    class Config:
        from_attributes = True


class ConceptResponse(BaseModel):
    id: int
    title: str
    explanation: str
    code_example: str
    unlocks_after_failures: int

    class Config:
        from_attributes = True


class ExerciseDetail(BaseModel):
    id: int
    title: str
    problem_statement: str
    scenario: str
    input_description: str
    expected_output_description: str
    starter_code: str
    tags: List[str]
    difficulty: str
    xp_reward: int
    allowed_imports: List[str]
    timeout_secs: int
    order_in_level: int
    is_completed: bool
    attempt_count: int
    visible_test_cases: List[VisibleTestCase]
    unlocked_hints: List[HintResponse]
    concepts: List[ConceptResponse]

    class Config:
        from_attributes = True


# ─── Submissions ──────────────────────────────────────────────────────────────
class SubmissionCreate(BaseModel):
    code: str
    custom_input: Optional[str] = None


class TestResultItem(BaseModel):
    test_case_id: int
    is_hidden: bool
    passed: bool
    feedback: Optional[str]
    execution_time_ms: float


class SubmissionResponse(BaseModel):
    id: int
    passed: bool
    test_results: List[TestResultItem]
    xp_awarded: int
    total_xp: int
    execution_time_ms: float
    attempt_count: int
    failure_message: Optional[str]
    hints_unlocked: int


# ─── Run Output ───────────────────────────────────────────────────────────────
class RunOutput(BaseModel):
    stdout: str
    stderr: str
    execution_time_ms: float
    error: str
    timed_out: bool


# ─── Achievements ─────────────────────────────────────────────────────────────
class AchievementResponse(BaseModel):
    id: int
    badge_type: str
    badge_name: str
    description: str
    earned_at: datetime

    class Config:
        from_attributes = True


# ─── Admin ────────────────────────────────────────────────────────────────────
class ExerciseCreate(BaseModel):
    level_id: int
    title: str
    problem_statement: str
    scenario: str = ""
    input_description: str = ""
    expected_output_description: str = ""
    starter_code: str = ""
    tags: List[str] = []
    difficulty: str = "easy"
    xp_reward: int = 10
    allowed_imports: List[str] = []
    timeout_secs: int = 5
    order_in_level: int = 0


class ExerciseUpdate(BaseModel):
    title: Optional[str] = None
    problem_statement: Optional[str] = None
    scenario: Optional[str] = None
    input_description: Optional[str] = None
    expected_output_description: Optional[str] = None
    starter_code: Optional[str] = None
    tags: Optional[List[str]] = None
    difficulty: Optional[str] = None
    xp_reward: Optional[int] = None
    allowed_imports: Optional[List[str]] = None
    timeout_secs: Optional[int] = None
    order_in_level: Optional[int] = None


class TestCaseCreate(BaseModel):
    exercise_id: int
    input_data: str = ""
    expected_output: str
    is_hidden: bool = True
    comparison_mode: str = "exact"
    order_num: int = 0


class AdminStats(BaseModel):
    total_users: int
    total_submissions: int
    total_exercises: int
    total_levels: int
    avg_pass_rate: float

