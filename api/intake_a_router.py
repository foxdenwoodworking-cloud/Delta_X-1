from fastapi import APIRouter, UploadFile, File
import json
from adapters.redis_adapter import get_redis
from orchestrator.queue_definitions import QUEUE_JOBS
from sentinel.client import notify_sentinel

router = APIRouter(prefix="/intake-a", tags=["intake_a"])

@router.post("/parse-pdf")
async def parse_pdf(file: UploadFile = File(...)):
    content = await file.read()
    job = {
        "type": "intake_a",
        "source": "api_a_pdf",
        "filename": file.filename,
        "payload": {"pdf_bytes": content.decode("latin1")}
    }

    redis = await get_redis()
    await redis.rpush(QUEUE_JOBS, json.dumps(job))
    await notify_sentinel("pdf_queued", {"filename": file.filename})

    return {"status": "queued", "file": file.filename}
