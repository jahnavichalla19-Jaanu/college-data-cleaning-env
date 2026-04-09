def easy(data):
    # basic: duplicates removed
    ids = [d["id"] for d in data]
    return 1.0 if len(ids) == len(set(ids)) else 0.5


def medium(data):
    # missing marks filled
    if all(d["marks"] is not None for d in data):
        return 1.0
    return 0.5


def hard(data):
    # full clean: format + marks
    correct = all(
        d["marks"] is not None and d["name"][0].isupper()
        for d in data
    )
    return 1.0 if correct else 0.5