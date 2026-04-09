def easy(data):
    ids = [d["id"] for d in data]
    return 1.0 if len(ids) == len(set(ids)) else 0.0


def medium(data):
    return 1.0 if all(d["marks"] is not None for d in data) else 0.0


def hard(data):
    return 1.0 if all(
        d["marks"] is not None and d["name"][0].isupper()
        for d in data
    ) else 0.0