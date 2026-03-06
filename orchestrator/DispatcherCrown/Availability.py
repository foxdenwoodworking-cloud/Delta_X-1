# Availability.py

# Placeholder registry — will be replaced by ScoutCrown integration
WORKER_REGISTRY = {
    "alpha": ["alpha", "alpha"],
    "Beta": ["Beta"],
    "Gamma": ["Gamma", "Gamma", "Gamma"]
    "Sigma": ["Sigma", "Sigma", "Sigma"]
    }

def choose_worker(species, capability, priority):
    # Later: integrate Scout Crown heartbeat + load sensing
    workers = WORKER_REGISTRY.get(species, [])

    if not workers:
        return None

    # Sovereign rule: paid jobs get first available worker
    if priority == "paid":
        return workers[0]

    # Extra jobs: round-robin
    if priority == "extra":
        return workers[-1]

    # Goodwill: lowest priority worker
    return workers[-1]
