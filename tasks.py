def easy(data):
    """Grader for easy task: check no duplicate IDs"""
    ids = [d["id"] for d in data]
    return 1.0 if len(ids) == len(set(ids)) else 0.0

def medium(data):
    """Grader for medium task: check no missing marks"""
    if all(d["marks"] is not None for d in data):
        return 1.0
    return 0.0

def hard(data):
    """Grader for hard task: check all names properly capitalized"""
    if all(d["name"] == d["name"].capitalize() for d in data):
        return 1.0
    return 0.0
