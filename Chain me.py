def chain(init_val, functions):
    result = init_val
    for func in functions:
        result = func(result)
    return result