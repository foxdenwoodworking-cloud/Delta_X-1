import json
from adapters.redis_adapter import get_redis
from .queue_definitions import QUEUE_JOBS
from worker.job_handlers.intake_a_job import handle_intake_a_job
from worker.job_handlers.intake_b_job import handle_intake_b_job
from sentinel.client import notify_sentinel

HANDLERS = {
    "intake_a": handle_intake_a_job,
    "intake_b": handle_intake_b_job,
}

async def dispatch_loop():
    redis = await get_redis()
    await notify_sentinel("dispatcher_started", {})

    while True:
        _, raw_job = await redis.blpop(QUEUE_JOBS)
        job = json.loads(raw_job)

        job_type = job.get("type")
        handler = HANDLERS.get(job_type)

        if handler:
            await handler(job)
        else:
            await notify_sentinel("unknown_job_type", {"type": job_type})
