def easy(data):
    ids = [d["id"] for d in data]
    unique = len(set(ids))
    total = len(ids)

    score = unique / total   # gradual score

    if score == 1.0:
        return 0.99
    elif score == 0.0:
        return 0.01
    return score


def medium(data):
    total = len(data)
    filled = sum(1 for d in data if d["marks"] is not None)

    score = filled / total

    if score == 1.0:
        return 0.99
    elif score == 0.0:
        return 0.01
    return score


def hard(data):
    total = len(data)
    correct = sum(1 for d in data if d["name"][0].isupper())

    score = correct / total

    if score == 1.0:
        return 0.99
    elif score == 0.0:
        return 0.01
    return score