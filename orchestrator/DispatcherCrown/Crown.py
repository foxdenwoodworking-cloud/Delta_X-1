# Crown.py

CROWN_NAME = "DispatcherCrown"
CROWN_VERSION = "1.0.0"
CROWN_ROLE = "sovereign_dispatcher"
CROWN_SCOPE = ["DroneWorker", "MARKETPLACE"]
CROWN_AUTHORITY = "route_and_assign"

from .routes import resolve_route
from .availability import choose_worker
from .priorities import normalize_priority

def handle(task):
    # 1. Determine route (species + capability + domain)
    route = resolve_route(task)

    # 2. Normalize priority (paid, extra, goodwill)
    priority = normalize_priority(task.get("priority"))

    # 3. Select worker based on availability
    worker = choose_worker(route["species"], route["capability"], priority)

    return {
        "crown": CROWN_NAME,
        "version": CROWN_VERSION,
        "species": route["species"],
        "capability": route["capability"],
        "domain": route["domain"],
        "priority": priority,
        "worker": worker,
        "payload": task.get("payload", {}),
        "timestamp": task.get("timestamp")
    }
