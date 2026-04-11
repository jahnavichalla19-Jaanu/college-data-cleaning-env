def easy(data):
    if not data:
        return 0.1
    ids = [d["id"] for d in data]
    score = len(set(ids)) / len(ids)
    return round(min(0.9, max(0.1, score)), 2)

def medium(data):
    if not data:
        return 0.1
    filled = sum(1 for d in data if d["marks"] is not None)
    score = filled / len(data)
    return round(min(0.9, max(0.1, score)), 2)

def hard(data):
    if not data:
        return 0.1
    correct = sum(1 for d in data if d["name"] == d["name"].capitalize())
    score = correct / len(data)
    return round(min(0.9, max(0.1, score)), 2)