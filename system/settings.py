import os
from .env_loader import load_env

# Load .env if present
load_env()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql://postgres:postgres@localhost:5432/delta")
SENTINELXL_WEBHOOK = os.getenv("SENTINELXL_WEBHOOK", "")
SENTINELXL_ENABLED = os.getenv("SENTINELXL_ENABLED", "false").lower() == "true"
