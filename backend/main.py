from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
import uuid
import sys
import asyncio

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from database import engine, Base
from routers import auth, users, levels, exercises, submissions, progress, achievements, admin, ai

# Create all tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DevOps Python Forge API",
    description="Backend for the DevOps Python Forge learning platform",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())[:8]
    start = time.time()
    response = await call_next(request)
    duration = round((time.time() - start) * 1000, 2)
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Response-Time"] = f"{duration}ms"
    return response


@app.get("/health")
def health():
    return {"status": "ok", "service": "DevOps Python Forge API"}


# Mount routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(levels.router, prefix="/api/levels", tags=["levels"])
app.include_router(exercises.router, prefix="/api/exercises", tags=["exercises"])
app.include_router(submissions.router, prefix="/api/submissions", tags=["submissions"])
app.include_router(progress.router, prefix="/api/progress", tags=["progress"])
app.include_router(achievements.router, prefix="/api/achievements", tags=["achievements"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(ai.router)
