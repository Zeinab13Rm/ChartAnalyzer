# src/infrastructure/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from src.config import settings

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Log SQL queries (disable in production)
    pool_size=10,
    max_overflow=20
)

# Async session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


chart_analyzer/                  # Project root
├── docker-compose.yml
├── Dockerfile
├── generate.sh
├── requirements.txt
├── alembic.ini                 # ✅ At root
├── alembic/                    # ✅ At root
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── src/                        # ✅ Only one src
│   ├── application/            # Use cases, services
│   ├── domain/                 # Entities, business logic
│   ├── infrastructure/         # DB, adapters, external services
│   │   ├── adapters/
│   │   │   ├── sqlmodel.py     # Your Base, models
│   │   │   └── __init__.py
│   │   └── persistence/        # DB session, engine
│   │       ├── database.py
│   │       └── __init__.py
│   ├── presentation/           # FastAPI routers, DTOs
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── users.py
│   │   │   │   └── charts.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── main.py                 # FastAPI app factory
│   └── config.py               # Config, settings
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── .env
├── .gitignore
└── README.md