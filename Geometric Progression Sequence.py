def geometric_sequence_elements(a, r, n):
    ls = [str(a)]
    for i in range(n - 1):
        a = a * r
        ls.append(str(a))
    
    result = ', '.join(ls)
    
    return result