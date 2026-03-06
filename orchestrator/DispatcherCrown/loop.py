import json
from adapters.redis_adapter import get_redis
from orchestrator.queue_definitions import QUEUE_JOBS
from .router import resolve
from .telemetry import emit
from .availability import worker_available

async def run():
    redis = await get_redis()
    await emit("dispatcher_started")

    while True:
        _, raw_job = await redis.blpop(QUEUE_JOBS)
        job = json.loads(raw_job)

        job_type = job.get("type")
        handler = resolve(job_type)

        if not handler:
            await emit("unknown_job_type", {"type": job_type})
            continue

        if not worker_available(job):
            await emit("no_worker_available", {"type": job_type})
            continue

        await handler(job)
