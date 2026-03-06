import aioredis
from .settings import REDIS_URL

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        _redis = await aioredis.from_url(
            REDIS_URL,
            encoding="utf-8",
            decode_responses=True
        )
    return _redis
