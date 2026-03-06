from worker.job_handlers.intake_a_job import handle_intake_a_job
from worker.job_handlers.intake_b_job import handle_intake_b_job
from sentinel.client import notify_sentinel

async def route_job(job: dict):
    job_type = job.get("type")

    if job_type == "intake_a":
        await notify_sentinel("intake_a_started", job)
        result = await handle_intake_a_job(job)
        await notify_sentinel("intake_a_finished", result)
        return result

    if job_type == "intake_b":
        await notify_sentinel("intake_b_started", job)
        result = await handle_intake_b_job(job)
        await notify_sentinel("intake_b_finished", result)
        return result

    await notify_sentinel("unknown_job_type", job)
    return {"status": "error", "message": f"Unknown job type: {job_type}"}
