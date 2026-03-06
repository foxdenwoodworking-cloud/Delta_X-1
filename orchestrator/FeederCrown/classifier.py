#!/usr/bin/env python3
# FeederCrown → Classifier
# Role: Assign each normalized job to a category for routing and submission.

class Classifier:
    def __init__(self):
        pass

    def run(self, job):
        """
        Classify a normalized job into a simple category.
        Placeholder logic: always returns 'general'.
        Replace with real classification rules or ML later.
        """
        if not job:
            return "unknown"

        title = (job.get("title") or "").lower()
        desc = (job.get("description") or "").lower()

        # Simple keyword-based stub
        if "python" in title or "python" in desc:
            return "python"
        if "data" in title or "data" in desc:
            return "data"
        if "api" in title or "api" in desc:
            return "api"

        return "general"
