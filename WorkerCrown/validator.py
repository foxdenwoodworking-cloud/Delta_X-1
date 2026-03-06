#!/usr/bin/env python3
# WorkerCrown → Validator
# Role: Ensure the incoming job has the minimum required structure.

class Validator:
    def __init__(self):
        pass

    def check(self, job):
        """
        Validate that the job contains the essential fields.
        Placeholder logic: requires an 'id' and some form of task/description.
        """
        if not job:
            return False

        if not job.get("id"):
            return False

        if not job.get("task") and not job.get("description"):
            return False

        return True
