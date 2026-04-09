def easy(data):
    """Grader: score 1.0 if no duplicate IDs exist"""
    if not data:
        return 0.0
    ids = [d["id"] for d in data]
    return 1.0 if len(ids) == len(set(ids)) else 0.0

def medium(data):
    """Grader: score 1.0 if no missing marks exist"""
    if not data:
        return 0.0
    return 1.0 if all(d["marks"] is not None for d in data) else 0.0

def hard(data):
    """Grader: score 1.0 if all names are properly capitalized"""
    if not data:
        return 0.0
    return 1.0 if all(d["name"] == d["name"].capitalize() for d in data) else 0.0