def deep_count(a):
    c = 0
    while a:
        p = a.pop()
        c += 1
        if type(p)==list:
            a.extend(p)
    return c