from fastapi import APIRouter
import json
from adapters.redis_adapter import get_redis
from orchestrator.queue_definitions import QUEUE_JOBS
from sentinel.client import notify_sentinel

router = APIRouter(prefix="/intake-b", tags=["intake_b"])

@router.post("/submit")
async def submit_payload(payload: dict):
    job = {
        "type": "intake_b",
        "source": "api_b_payload",
        "payload": payload
    }

    redis = await get_redis()
    await redis.rpush(QUEUE_JOBS, json.dumps(job))
    await notify_sentinel("payload_queued", {"source": "intake_b"})

    return {"status": "queued", "source": "intake_b"}
