def pattern(n):
    if n <= 0:
        return ''
    
    ls = []
    for i in range(1, n + 1):
        s = ''
        for j in range(i, n + 1):
            s += str(j)
        
        ls.append(s)
    
    return "\n".join(ls)