def reverse(a):
    st = ''.join(a)[::-1]
    
    l = []
    
    start = 0
    
    for s in a:
        lenght = len(s)
        l.append(st[start:start + lenght])
        start += lenght
    
    return l