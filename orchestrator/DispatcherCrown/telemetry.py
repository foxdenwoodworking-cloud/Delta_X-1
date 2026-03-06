from sentinel.client import notify_sentinel

async def emit(event, data=None):
    await notify_sentinel(event, data or {})
