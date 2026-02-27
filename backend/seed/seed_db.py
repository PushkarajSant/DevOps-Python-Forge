#!/usr/bin/env python3
"""
Master seed script: creates all levels, exercises, test cases, hints, and concepts.
Run: python seed/seed_db.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import SessionLocal, engine, Base
from models import Level, Exercise, TestCase, Hint, Concept

# Import exercise data
from seed.exercises.level_0 import LEVEL_0_EXERCISES
from seed.exercises.level_1 import LEVEL_1_EXERCISES
from seed.exercises.level_2 import LEVEL_2_EXERCISES
from seed.exercises.level_3 import LEVEL_3_EXERCISES
from seed.exercises.level_4 import LEVEL_4_EXERCISES
from seed.exercises.level_5 import LEVEL_5_EXERCISES
from seed.exercises.level_6 import LEVEL_6_EXERCISES
from seed.exercises.level_7 import LEVEL_7_EXERCISES
from seed.exercises.level_8_9_10 import LEVEL_8_EXERCISES, LEVEL_9_EXERCISES, LEVEL_10_EXERCISES

LEVELS = [
    {
        "level_number": 0,
        "title": "Python Execution Basics",
        "description": "Understand how Python runs and interacts with environment. Master print, input, and basic execution model.",
        "color": "#22c55e",
        "unlock_xp_required": 0,
        "min_exercises_to_pass": 7,
        "exercises": LEVEL_0_EXERCISES,
    },
    {
        "level_number": 1,
        "title": "Core Fundamentals",
        "description": "Variables, data types, type casting, operators, and string formatting in DevOps contexts.",
        "color": "#22c55e",
        "unlock_xp_required": 40,
        "min_exercises_to_pass": 15,
        "exercises": LEVEL_1_EXERCISES,
    },
    {
        "level_number": 2,
        "title": "Control Flow",
        "description": "Master if/elif/else, loops, break, and continue through real DevOps scenarios.",
        "color": "#22c55e",
        "unlock_xp_required": 200,
        "min_exercises_to_pass": 15,
        "exercises": LEVEL_2_EXERCISES,
    },
    {
        "level_number": 3,
        "title": "Data Structures",
        "description": "Lists, tuples, sets, and dictionaries — the core of all automation scripts.",
        "color": "#22c55e",
        "unlock_xp_required": 400,
        "min_exercises_to_pass": 18,
        "exercises": LEVEL_3_EXERCISES,
    },
    {
        "level_number": 4,
        "title": "Functions & Modular Thinking",
        "description": "Write reusable, testable, well-documented Python functions for DevOps automation.",
        "color": "#22c55e",
        "unlock_xp_required": 650,
        "min_exercises_to_pass": 15,
        "exercises": LEVEL_4_EXERCISES,
    },
    {
        "level_number": 5,
        "title": "File Handling & Log Processing",
        "description": "Read, write, and parse files — logs, JSON, CSV, YAML — the bread and butter of ops scripts.",
        "color": "#eab308",
        "unlock_xp_required": 950,
        "min_exercises_to_pass": 18,
        "exercises": LEVEL_5_EXERCISES,
    },
    {
        "level_number": 6,
        "title": "Error Handling & Logging",
        "description": "Production-grade exception handling, custom errors, logging patterns.",
        "color": "#eab308",
        "unlock_xp_required": 1300,
        "min_exercises_to_pass": 10,
        "exercises": LEVEL_6_EXERCISES,
    },
    {
        "level_number": 7,
        "title": "API & Networking",
        "description": "Call REST APIs, handle status codes, parse JSON responses, build automation integrations.",
        "color": "#eab308",
        "unlock_xp_required": 1600,
        "min_exercises_to_pass": 15,
        "exercises": LEVEL_7_EXERCISES,
    },
    {
        "level_number": 8,
        "title": "CLI Tools & Packaging",
        "description": "Build professional CLI tools with argparse, modular structure, and clean packaging.",
        "color": "#f97316",
        "unlock_xp_required": 2000,
        "min_exercises_to_pass": 15,
        "exercises": LEVEL_8_EXERCISES,
    },
    {
        "level_number": 9,
        "title": "Concurrency & Performance",
        "description": "Threading, multiprocessing, asyncio basics, and performance profiling.",
        "color": "#ef4444",
        "unlock_xp_required": 2450,
        "min_exercises_to_pass": 10,
        "exercises": LEVEL_9_EXERCISES,
    },
    {
        "level_number": 10,
        "title": "Capstone Projects",
        "description": "Complete production-grade projects combining all skills. Real-world DevOps automation systems.",
        "color": "#ef4444",
        "unlock_xp_required": 2800,
        "min_exercises_to_pass": 3,
        "exercises": LEVEL_10_EXERCISES,
    },
]


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Clear existing data (order matters due to FK constraints)
        db.query(Concept).delete()
        db.query(Hint).delete()
        db.query(TestCase).delete()
        db.query(Exercise).delete()
        db.query(Level).delete()
        db.commit()

        total_exercises = 0
        for level_data in LEVELS:
            exercises_data = level_data.pop("exercises")
            level = Level(**level_data)
            db.add(level)
            db.flush()  # Get level.id

            for order, ex_data in enumerate(exercises_data, start=1):
                test_cases_data = ex_data.pop("test_cases", [])
                hints_data = ex_data.pop("hints", [])
                concepts_data = ex_data.pop("concepts", [])

                exercise = Exercise(
                    level_id=level.id,
                    order_in_level=order,
                    **ex_data,
                )
                db.add(exercise)
                db.flush()

                for tc_data in test_cases_data:
                    tc = TestCase(exercise_id=exercise.id, **tc_data)
                    db.add(tc)

                for hint_data in hints_data:
                    hint = Hint(exercise_id=exercise.id, **hint_data)
                    db.add(hint)

                for concept_data in concepts_data:
                    concept = Concept(exercise_id=exercise.id, **concept_data)
                    db.add(concept)

                total_exercises += 1

        db.commit()
        print(f"✓ Seeded {len(LEVELS)} levels and {total_exercises} exercises successfully.")

    except Exception as e:
        db.rollback()
        print(f"✗ Seed failed: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed()
