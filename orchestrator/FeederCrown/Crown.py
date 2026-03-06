#!/usr/bin/env python3
# Crown: FeederCrown
# Role: External job intake → normalization → classification → submission
# Sovereign Operator: Aaron

from .ai_adapter import AIAdapter
from .marketplace_adapter import MarketplaceAdapter
from .normalize import Normalizer
from .classifier import Classifier
from .submit import Submitter
from .telemetry import Telemetry


class FeederCrown:
    def __init__(self):
        self.ai = AIAdapter()
        self.market = MarketplaceAdapter()
        self.normalizer = Normalizer()
        self.classifier = Classifier()
        self.submitter = Submitter()
        self.telemetry = Telemetry()

    def pulse(self):
        """Main loop: fetch → normalize → classify → submit → log."""
        raw_jobs = self.market.fetch_jobs()
        if not raw_jobs:
            self.telemetry.log("No jobs available.")
            return

        for job in raw_jobs:
            normalized = self.normalizer.run(job)
            category = self.classifier.run(normalized)
            result = self.submitter.run(normalized, category)
            self.telemetry.log(f"Processed job: {result}")

    def run_once(self):
        """Single execution cycle."""
        try:
            self.pulse()
        except Exception as e:
            self.telemetry.error(f"FeederCrown error: {e}")
