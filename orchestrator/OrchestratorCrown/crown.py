from sentinel.client import notify_sentinel

class OrchestratorCrown:
    name = "OrchestratorCrown"
    version = "1.0.0"
    domain = "orchestrator"
    authority = ["environment", "lineage"]

    @staticmethod
    async def register_environment():
        await notify_sentinel(
            "orchestrator_environment",
            {
                "crown": OrchestratorCrown.name,
                "version": OrchestratorCrown.version,
                "domain": OrchestratorCrown.domain,
                "status": "sovereign_ready"
            }
        )

    @staticmethod
    async def announce_ready():
        await notify_sentinel(
            "orchestrator_ready",
            {
                "crown": OrchestratorCrown.name,
                "status": "ready_for_dispatch"
            }
        )

    @staticmethod
    async def heartbeat():
        await notify_sentinel(
            "orchestrator_heartbeat",
            {
                "crown": OrchestratorCrown.name,
                "status": "alive"
            }
        )
