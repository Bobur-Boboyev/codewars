def reverse_and_mirror(s1, s2):
    s = ''
    for i in s2[::-1]:
        if i.isupper():
            s += i.lower()
        else:
            s += i.upper()
    s += '@@@'
    s1 = s1[::-1]+s1
    for i in s1:
        if i.isupper():
            s += i.lower()
        else:
            s += i.upper()
    return s