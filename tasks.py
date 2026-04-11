def easy(data):

    ids = [d["id"] for d in data]
    if len(ids) == len(set(ids)):
        return 1.0
    return 0.0


def medium(data):
    
    total = len(data)
    filled = sum(1 for d in data if d["marks"] is not None)
    return filled / total


def hard(data):

    total = len(data)
    correct = sum(1 for d in data if d["name"][0].isupper())
    return correct / total