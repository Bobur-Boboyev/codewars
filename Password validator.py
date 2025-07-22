def password(st):
    if len(st) < 8:
        return False
    a = 0
    l = 0
    d = 0
    for i in st:
        if i.isupper():
            a += 1
        if i.islower():
            l +=1 
        if i.isdigit():
            d += 1
    return a >= 1 and l >= 1 and d >= 1