#!/usr/bin/env python3
# FeederCrown → Normalizer
# Role: Convert raw marketplace job payloads into a consistent internal format.

class Normalizer:
    def __init__(self):
        pass

    def run(self, job):
        """
        Normalize raw job data into a stable internal structure.
        This keeps downstream components predictable.
        """
        if not job:
            return {}

        return {
            "id": job.get("id"),
            "title": job.get("title", "").strip(),
            "description": job.get("description", "").strip(),
            "source": job.get("source"),
            "raw": job
        }
