def work_on_strings(a, b):
    dct_a = {}
    dct_b = {}
    for i in a:
        key = i.lower()
        if key in dct_a:
            dct_a[key] += 1
        else:
            dct_a[key] = 1
    for j in b:
        key = j.lower()
        if key in dct_b:
            dct_b[key] += 1
        else:
            dct_b[key] = 1
    s1 = ''
    for ch in a:
        if ch.lower() in dct_b and dct_b[ch.lower()] % 2 != 0:
            s1 += ch.swapcase()
        else:
            s1 += ch
    s2 = ''
    for ch in b:
        if ch.lower() in dct_a and dct_a[ch.lower()] % 2 != 0:
            s2 += ch.swapcase()
        else:
            s2 += ch

    return s1 + s2