def easy(data):
    """Grader: Remove duplicates — scores between 0.001 and 0.999"""
    if not data:
        return 0.2
    ids = [d["id"] for d in data]
    unique = len(set(ids))
    total = len(ids)
    if unique == total:
        return 0.999
    score = unique / total
    return round(max(0.001, min(0.999, score)), 3)


def medium(data):
    """Grader: Fill missing marks — scores between 0.001 and 0.999"""
    if not data:
        return 0.2
    filled = sum(1 for d in data if d["marks"] is not None)
    total = len(data)
    score = filled / total
    if score >= 1.0:
        return 0.999
    return round(max(0.001, min(0.998, score)), 3)


def hard(data):
    """Grader: Fix name formatting — scores between 0.001 and 0.999"""
    if not data:
        return 0.2
    correct = sum(1 for d in data if d["name"] == d["name"].capitalize())
    total = len(data)
    score = correct / total
    if score >= 1.0:
        return 0.999
    return round(max(0.001, min(0.998, score)), 3)