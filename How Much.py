def howmuch(m, n):
    ls = []
    
    for i in range(min(m,n), max(m, n) + 1):
        b = (i - 2) // 7
        c = (i - 1) // 9
        
        if i - (7 * b) == 2 and i - (9 * c) == 1:
            template = [f"M: {i}", f"B: {b}", f"C: {c}"]
            ls.append(template)
    
    return ls
