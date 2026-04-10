def easy(data):
    """Grader: Remove duplicates - partial scoring"""
    if not data:
        return 0.2
    ids = [d["id"] for d in data]
    if len(ids) == len(set(ids)):
        return 0.8
    return 0.2


def medium(data):
    """Grader: Fill missing marks - partial scoring"""
    if not data:
        return 0.2
    filled = sum(1 for d in data if d["marks"] is not None)
    total = len(data)
    score = filled / total
    if score == 0:
        return 0.2
    if score == 1:
        return 0.8
    return round(score, 2)


def hard(data):
    """Grader: Fix name format - partial scoring"""
    if not data:
        return 0.2
    score = 0.0
    if all(d["marks"] is not None for d in data):
        score += 0.4
    if all(d["name"][0].isupper() for d in data):
        score += 0.4
    if score == 0:
        return 0.2
    return round(score, 2)