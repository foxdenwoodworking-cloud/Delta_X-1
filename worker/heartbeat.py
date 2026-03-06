import asyncio
import time
from sentinel.client import notify_sentinel

async def heartbeat():
    while True:
        ts = time.time()
        print(f"[HEARTBEAT] Worker alive at {ts}")
        await notify_sentinel("worker_heartbeat", {"timestamp": ts})
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(heartbeat())
