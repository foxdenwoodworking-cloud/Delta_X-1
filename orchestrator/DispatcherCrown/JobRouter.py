def map_task_to_species(task):
    t = task.get("type", "").upper()

    if t == "AI_SUMMARY":
        return Beta", "compress_prompt"

    if t in ["Drones_CLASSIFY", "Drones_ANALYZE", "DroneWorker_AUTOMATION"]:
        return "Alpha", "analyze"

    if t == "AI_GENERATE":
        return "Gamma", "transform"

    return "Alpha", "analyze"
