from worker.job_handlers.intake_a_job import handle_intake_a_job
from worker.job_handlers.intake_b_job import handle_intake_b_job

ROUTES = {
    "intake_a": handle_intake_a_job,
    "intake_b": handle_intake_b_job,
}

def resolve(job_type: str):
    return ROUTES.get(job_type)
