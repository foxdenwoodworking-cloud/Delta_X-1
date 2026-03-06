import json
from adapters.redis_adapter import get_redis
from .queue_definitions import QUEUE_JOBS, QUEUE_RESULTS
from sentinel.client import notify_sentinel

async def route_job(job: dict):
    redis = await get_redis()

    await redis.rpush(QUEUE_JOBS, json.dumps(job))
    await notify_sentinel("job_routed", {"type": job.get("type")})

    return {"status": "queued", "type": job.get("type")}
