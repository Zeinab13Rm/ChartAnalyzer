# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from alembic import context
import asyncio
import sys
import os

# Add the project root to sys.path to import your models
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import your Base from your app
from src.infrastructure.adapters.sqlserver import Base

# ------------------------------
# Configure Alembic
# ------------------------------
config = context.config

# Setup logging (if you have it in alembic.ini)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata for autogenerate
target_metadata = Base.metadata


# ------------------------------
# Offline Mode (no DB connection)
# ------------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ------------------------------
# Online Mode (with async engine)
# ------------------------------
async def run_async_migrations() -> None:
    """Create and run async migrations."""
    connectable: AsyncEngine = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        # ✅ Correct: Configure context inside run_sync
        await connection.run_sync(lambda conn: context.configure(
            connection=conn,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        ))

        # ✅ Correct: Wrap run_migrations in lambda to avoid extra arg
        await connection.run_sync(lambda conn: context.run_migrations())

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())


# ------------------------------
# Choose mode
# ------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()