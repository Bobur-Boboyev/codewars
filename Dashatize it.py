def dashatize(n):
    n = abs(n)
    n = str(n)
    v = ''
    for i in n:
        if int(i) % 2 == 1:
            v += f'-{i}-'
        else:
            v += i
    v= v.replace('--', '-')
    if v[0]=='-':
        v = v[1:]
    if v[-1]=='-':
        v = v[:-1]
    return v
