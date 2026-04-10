def easy(data):
    """Grader: Remove duplicates — no duplicate IDs"""
    if not data:
        return 0.2
    ids = [d["id"] for d in data]
    if len(ids) == len(set(ids)):
        return 0.999
    duplicates = len(ids) - len(set(ids))
    return round(max(0.001, 0.8 - (duplicates * 0.2)), 3)


def medium(data):
    """Grader: Fill missing marks — no None values"""
    if not data:
        return 0.2
    filled = sum(1 for d in data if d["marks"] is not None)
    total = len(data)
    score = filled / total
    if score >= 1.0:
        return 0.999
    if score <= 0:
        return 0.001
    return round(score, 3)


def hard(data):
    """Grader: Fix name format — all names capitalized"""
    if not data:
        return 0.2
    correct = sum(1 for d in data if d["name"] == d["name"].capitalize())
    total = len(data)
    score = correct / total
    if score >= 1.0:
        return 0.999
    if score <= 0:
        return 0.001
    return round(score, 3)