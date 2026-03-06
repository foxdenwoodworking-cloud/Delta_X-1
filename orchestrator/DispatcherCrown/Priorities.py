# Priorities.py

def normalize_priority(raw):
    if not raw:
        return "normal"

    raw = raw.lower()

    if raw in ["paid", "p1", "high"]:
        return "paid"

    if raw in ["extra", "p2", "medium"]:
        return "extra"

    if raw in ["goodwill", "p3", "low"]:
        return "goodwill"

    return "normal"
