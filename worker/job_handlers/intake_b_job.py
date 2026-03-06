async def handle_intake_b_job(job: dict):
    payload = job.get("payload", {})
    return {"status": "ok", "path": "intake_b", "payload": payload}
