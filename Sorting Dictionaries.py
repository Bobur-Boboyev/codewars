def sort_dict(d: dict):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)