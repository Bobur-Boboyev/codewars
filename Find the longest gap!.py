def gap(num):
    if num == 0:
        return 0
    
    b = bin(num)[2:]
    r = b[::-1]
    i = r.find('1')
    bn = r[i:][::-1]
    
    ls = bn.replace('1', ' ').split()
    
    if not ls:
        return 0
    
    result = len(max(ls, key=len))
    
    return result