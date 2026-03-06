import asyncpg
from .settings import POSTGRES_DSN

async def get_postgres():
    return await asyncpg.connect(POSTGRES_DSN)
