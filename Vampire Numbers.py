def vampire_test(x, y):
    m, x, y = str(x * y), str(x), str(y)
    
    z = x + y
    
    return sorted(m) == sorted(z)