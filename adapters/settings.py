import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://delta:delta@localhost:5432/delta_sxl")

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

SENTINELXL_WEBHOOK = os.getenv("SENTINELXL_WEBHOOK", "")
SENTINELXL_ENABLED = bool(SENTINELXL_WEBHOOK)
