def easy(data):
    ids = [d["id"] for d in data]
    unique = len(set(ids))
    total = len(ids)

    score = unique / total   # gradual score

    if score == 1.0:
        return 0.3


def medium(data):
    total = len(data)
    filled = sum(1 for d in data if d["marks"] is not None)

    score = filled / total

    if score == 1.0:
        return 0.5


def hard(data):
    total = len(data)
    correct = sum(1 for d in data if d["name"][0].isupper())

    score = correct / total

    if score == 1.0:
        return 0.8