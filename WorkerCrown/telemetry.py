#!/usr/bin/env python3
# WorkerCrown → Telemetry
# Role: Lightweight logging for WorkerCrown operations.

import datetime

class Telemetry:
    def __init__(self):
        pass

    def _stamp(self):
        return datetime.datetime.utcnow().isoformat()

    def log(self, message):
        print(f"[INFO] {self._stamp()} | {message}")

    def error(self, message):
        print(f"[ERROR] {self._stamp()} | {message}")
