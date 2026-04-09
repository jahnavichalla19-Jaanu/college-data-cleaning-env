def easy(data):
    """Grader: no duplicate IDs"""
    ids = [d["id"] for d in data]
    return 1.0 if len(ids) == len(set(ids)) else 0.0

def medium(data):
    """Grader: no missing marks"""
    return 1.0 if all(d["marks"] is not None for d in data) else 0.0

def hard(data):
    """Grader: all names properly capitalized"""
    return 1.0 if all(d["name"] == d["name"].capitalize() for d in data) else 0.0