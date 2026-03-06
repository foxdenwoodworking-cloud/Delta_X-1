import asyncio
from sentinel.client import notify_sentinel
from orchestrator.OrchestratorCrown.crown import OrchestratorCrown
from orchestrator.DispatcherCrown.loop import run as dispatcher_run

async def main():
    await notify_sentinel("orchestrator_starting")
    await OrchestratorCrown.register_environment()
    await OrchestratorCrown.announce_ready()
    await dispatcher_run()

if __name__ == "__main__":
    asyncio.run(main())
