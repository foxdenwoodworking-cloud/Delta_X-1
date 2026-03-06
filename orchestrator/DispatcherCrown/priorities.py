def normalize(priority: str):
    table = {
        "paid": 1,
        "extra": 2,
        "normal": 3,
        "goodwill": 4,
    }
    return table.get(priority, 3)
