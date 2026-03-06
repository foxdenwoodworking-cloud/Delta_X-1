async def handle_intake_a_job(job: dict):
    payload = job.get("payload", {})
    return {"status": "ok", "path": "intake_a", "payload": payload}

