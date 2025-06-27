def is_triangular(t):
    if t == 1:
        return True
    a = 1
    for i in range(2, t+1):
        a += i
        if a == t:
            return True
    return False