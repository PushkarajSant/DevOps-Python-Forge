# DevOps Python Forge ⚙️🐍

A production-grade, exercise-driven Python learning platform for DevOps engineers. Master Python through **193 hands-on exercises** across 11 levels — from "Hello World" to building CLI tools and async scripts.

## Features

- 🎯 **193 Exercises** across 11 progressive levels
- 🖥️ **Monaco Editor IDE** — VS Code-like coding experience in the browser
- 🔒 **Sandboxed Execution** — AST-validated, timeout-protected Python runner
- 🏆 **Gamification** — XP, streaks, levels, leaderboard, and 16 achievement badges
- 💡 **Progressive Hints** — unlock after failed attempts (no solution spoilers)
- 📊 **Progress Dashboard** — per-level breakdown, activity heatmap, stats
- 🛡️ **Admin Panel** — exercise CRUD, user management, platform stats
- 🔐 **JWT Authentication** — secure user sessions
- 🐳 **Docker Ready** — single `docker-compose up` deployment

## Tech Stack

| Layer | Tech |
|-------|------|
| Frontend | Next.js 14, TypeScript, Tailwind CSS, Monaco Editor |
| Backend | FastAPI, Python 3.11+ |
| Database | SQLite + SQLAlchemy ORM |
| Auth | JWT (python-jose + passlib/bcrypt) |
| Execution | subprocess + AST validation sandbox |

## Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm / yarn

### Backend Setup

```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate        # Windows
# source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
python seed/seed_db.py
uvicorn main:app --reload --port 8000
```

### Frontend Setup

```powershell
cd frontend
npm install
npm run dev
```

Then open **http://localhost:3000** in your browser.

### Docker (Alternative)

```bash
docker-compose up --build
```

## Project Structure

```
devops-python-forge/
├── backend/
│   ├── main.py                  # FastAPI entry
│   ├── models.py                # SQLAlchemy ORM models
│   ├── schemas.py               # Pydantic request/response schemas
│   ├── security.py              # JWT + password hashing
│   ├── database.py              # DB setup
│   ├── routers/                 # API route modules
│   │   ├── auth.py              # Register, login, me
│   │   ├── levels.py            # Level listing + exercises
│   │   ├── exercises.py         # Exercise detail
│   │   ├── submissions.py       # Run + submit code
│   │   ├── progress.py          # Dashboard + stats
│   │   ├── achievements.py      # Badge system
│   │   ├── admin.py             # Admin CRUD
│   │   └── users.py             # Leaderboard
│   ├── execution/               # Code execution engine
│   │   ├── runner.py            # Sandboxed subprocess runner
│   │   ├── comparator.py        # Output comparison (5 modes)
│   │   └── feedback.py          # Failure analysis engine
│   └── seed/                    # Database seeding
│       ├── seed_db.py           # Seed runner script
│       └── exercises/           # Level 0–10 exercise data
├── frontend/
│   └── src/
│       ├── app/                 # Next.js pages
│       │   ├── page.tsx         # Login/Register
│       │   ├── dashboard/       # Dashboard + level grid
│       │   ├── levels/          # Exercise list per level
│       │   ├── exercise/        # Monaco IDE + run/submit
│       │   ├── progress/        # Stats + heatmap
│       │   ├── leaderboard/     # XP ranking
│       │   ├── achievements/    # Badges
│       │   └── admin/           # Admin panel
│       ├── context/             # AuthContext
│       └── lib/                 # API client
└── docker-compose.yml           # Multi-container setup
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register` | POST | Create account |
| `/api/auth/login` | POST | Get JWT token |
| `/api/auth/me` | GET | Current user info |
| `/api/levels` | GET | All levels + progress |
| `/api/levels/{n}/exercises` | GET | Exercises for level |
| `/api/exercises/{id}` | GET | Exercise detail with hints |
| `/api/submissions/{id}/run` | POST | Run code (sandbox) |
| `/api/submissions/{id}/submit` | POST | Submit solution |
| `/api/progress/dashboard` | GET | User stats |
| `/api/achievements` | GET | User badges |
| `/api/users/leaderboard` | GET | XP ranking |
| `/api/admin/*` | Various | Admin operations |

## Exercise Levels

| Level | Topic | Exercises |
|-------|-------|-----------|
| 0 | Python Execution Basics | 10 |
| 1 | Core Fundamentals | 20 |
| 2 | Control Flow Mastery | 20 |
| 3 | Data Structures | 25 |
| 4 | Functions & Modularity | 20 |
| 5 | File Handling & I/O | 25 |
| 6 | Error Handling | 15 |
| 7 | API & Networking | 20 |
| 8 | CLI Tools | 20 |
| 9 | Concurrency & Async | 15 |
| 10 | Capstone Projects | 5 |

## Security

The execution engine prevents malicious code via:
- **AST scanning** — blocks `os.system`, `subprocess`, `socket`, `eval`, `exec`
- **Per-exercise import whitelist**
- **5-second timeout** with infinite loop detection
- **Output size cap** (10KB)
- **Isolated subprocess** — no file system or network access

## License

MIT
