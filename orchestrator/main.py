from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import uuid
import time

app = FastAPI(
    title="Delta_X-1 Orchestrator",
    version="1.0.0",
    description="Primary job intake + worker coordination service."
)

# In-memory job store (runtime only)
JOBS = {}
WORKER_HEARTBEATS = {}

class JobRequest(BaseModel):
    payload: dict

class JobResult(BaseModel):
    job_id: str
    result: dict

@app.get("/")
async def root():
    return {
        "service": "Delta_X-1 Orchestrator",
        "status": "running",
        "public_port": 8000
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/submit")
async def submit_job(job: JobRequest):
    job_id = str(uuid.uuid4())
    JOBS[job_id] = {
        "payload": job.payload,
        "status": "queued",
        "result": None,
        "created_at": time.time()
    }
    return {"job_id": job_id, "status": "queued"}

@app.get("/claim")
async def claim_job(worker_id: str):
    for job_id, data in JOBS.items():
        if data["status"] == "queued":
            data["status"] = "claimed"
            data["claimed_by"] = worker_id
            return {"job_id": job_id, "payload": data["payload"]}
    return {"job_id": None}

@app.post("/complete")
async def complete_job(result: JobResult):
    if result.job_id not in JOBS:
        return {"error": "invalid job_id"}

    JOBS[result.job_id]["status"] = "complete"
    JOBS[result.job_id]["result"] = result.result
    return {"status": "stored"}

@app.post("/heartbeat")
async def heartbeat(worker_id: str):
    WORKER_HEARTBEATS[worker_id] = time.time()
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
