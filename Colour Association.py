def colour_association(arr):
    result = list(map(lambda x: {x[0]: x[1]}, arr))
    return result