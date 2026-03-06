#!/usr/bin/env python3
# FeederCrown → MarketplaceAdapter
# Role: Connect to external job sources and return raw job payloads.

class MarketplaceAdapter:
    def __init__(self):
        pass

    def fetch_jobs(self):
        """
        Fetch raw jobs from external marketplaces or APIs.
        This is a placeholder returning an empty list to keep the pipeline stable.
        Replace with real API calls when wiring external sources.
        """
        return []

    def fetch_single(self, job_id):
        """
        Optional: fetch a single job by ID.
        Placeholder for future marketplace integrations.
        """
        return None
