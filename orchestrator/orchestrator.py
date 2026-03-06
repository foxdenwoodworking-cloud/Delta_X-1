import asyncio
import json
from adapters.redis_adapter import get_redis
from .queue_definitions import QUEUE_JOBS, QUEUE_RESULTS
from .job_router import route_job
from sentinel.client import notify_sentinel

async def orchestrator_loop():
    redis = await get_redis()
    await notify_sentinel("orchestrator_started", {})

    while True:
        _, raw_job = await redis.blpop(QUEUE_JOBS)
        job = json.loads(raw_job)

        result = await route_job(job)
        await redis.rpush(QUEUE_RESULTS, json.dumps(result))

        await asyncio.sleep(0.01)

if __name__ == "__main__":
    asyncio.run(orchestrator_loop())
