def changer(s):
    s = s.lower()
    st = ''
    for i in s:
        if i.isalpha():
            a = ord(i)+1
            if a > 122:
                a = 97
            st+= chr(a)
        else:
            st+=i
    return ''.join([i.upper() if i in 'aeuio' else i for i in st])