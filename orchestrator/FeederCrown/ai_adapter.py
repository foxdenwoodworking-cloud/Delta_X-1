#!/usr/bin/env python3
# FeederCrown → AIAdapter
# Role: Provide LLM-powered enrichment, rewriting, or extraction for job data.

class AIAdapter:
    def __init__(self):
        pass

    def enhance(self, job):
        """
        Optional enrichment step.
        Could rewrite descriptions, extract skills, or clean text.
        Currently a passthrough to keep the pipeline deterministic.
        """
        return job

    def summarize(self, text):
        """
        Optional summarization hook.
        Placeholder for future LLM integration.
        """
        return text[:500] if text else ""
