#!/usr/bin/env python3
# WorkerCrown → WorkerAdapter
# Role: Transform a validated job into an execution‑ready payload.

class WorkerAdapter:
    def __init__(self):
        pass

    def prepare(self, job):
        """
        Convert the normalized job into a format the Runner can execute.
        Placeholder logic: shallow copy with stable keys.
        """
        if not job:
            return {}

        return {
            "id": job.get("id"),
            "task": job.get("task") or job.get("description"),
            "meta": job
        }
