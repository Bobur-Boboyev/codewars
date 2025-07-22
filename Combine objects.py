def combine(*objects):
    r = {}
    for obj in objects:
        for key,value in obj.items():
            if key in r:
                r[key] += value
            else:
                r[key] = value
    return r