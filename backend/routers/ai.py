from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, Any
from pydantic import BaseModel
import os
from openai import AsyncOpenAI

from database import get_db
from models import User, Exercise
from routers.auth import get_current_user

router = APIRouter(prefix="/api/ai", tags=["ai"])

# Point OpenAI client to local Ollama instance running in Docker
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:1.5b")

client = AsyncOpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama" # required but ignored by ollama
)

class AIRequest(BaseModel):
    exercise_id: int
    code: str
    error_message: str | None = None

@router.post("/review")
async def request_code_review(
    req: AIRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Provides a senior-level code review for passed exercises."""
    exercise = db.query(Exercise).filter(Exercise.id == req.exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    system_prompt = (
        "You are a Senior DevOps Engineer reviewing code from a junior engineer. "
        "The code already passes all functional tests, so your job is NOT to fix bugs. "
        "Your job is to review the code for production readiness, efficiency, readability, "
        "and Pythonic best practices. Be concise, direct, and professional."
    )
    
    user_prompt = (
        f"Exercise Statement:\n{exercise.problem_statement}\n\n"
        f"Junior Engineer's Solution:\n```python\n{req.code}\n```\n\n"
        "Please provide a brief code review."
    )

    try:
        response = await client.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            max_tokens=600
        )
        return {"review": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")

@router.post("/hint")
async def request_mentor_hint(
    req: AIRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Provides a logical hint without writing code for stuck users."""
    exercise = db.query(Exercise).filter(Exercise.id == req.exercise_id).first()
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    system_prompt = (
        "You are a technical mentor for a DevOps engineer who is currently stuck on a Python exercise. "
        "UNDER NO CIRCUMSTANCES should you write or provide the actual Python code to solve the problem. "
        "You must ONLY provide a conceptual hint, explain a logical flaw, or point them toward a built-in feature/method "
        "that they should research."
    )
    
    user_prompt = (
        f"Exercise Statement:\n{exercise.problem_statement}\n\n"
        f"My Current Code:\n```python\n{req.code}\n```\n\n"
        f"The error/failure I am getting is:\n{req.error_message or 'It fails the test cases.'}\n\n"
        "Please give me a hint on what I am doing wrong."
    )

    try:
        response = await client.chat.completions.create(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.4,
            max_tokens=400
        )
        return {"hint": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service unavailable: {str(e)}")
