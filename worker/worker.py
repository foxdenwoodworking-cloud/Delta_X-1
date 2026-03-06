import asyncio
import json
from adapters.redis_adapter import get_redis
from orchestrator.queue_definitions import QUEUE_RESULTS
from sentinel.client import notify_sentinel

async def worker_loop():
    redis = await get_redis()
    await notify_sentinel("worker_started", {})

    while True:
        _, raw_result = await redis.blpop(QUEUE_RESULTS)
        result = json.loads(raw_result)

        print(f"[WORKER] Completed job: {result}")
        await notify_sentinel("worker_processed_result", result)

        await asyncio.sleep(0.01)

if __name__ == "__main__":
    asyncio.run(worker_loop())
