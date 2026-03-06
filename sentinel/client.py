import aiohttp
from adapters.settings import SENTINELXL_WEBHOOK, SENTINELXL_ENABLED

async def notify_sentinel(event: str, payload: dict | None = None):
    if not SENTINELXL_ENABLED or not SENTINELXL_WEBHOOK:
        return

    data = {"event": event, "payload": payload or {}}

    async with aiohttp.ClientSession() as session:
        try:
            await session.post(SENTINELXL_WEBHOOK, json=data, timeout=5)
        except Exception:
            pass
