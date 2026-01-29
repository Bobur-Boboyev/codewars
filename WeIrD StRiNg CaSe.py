def to_weird_case(words):
    words = words.split()
    st = ''
    for word in words:
        s = ''
        for ind, item in enumerate(word):
            if ind % 2 == 0:
                s += item.upper()
            else:
                s += item.lower()
        st += s + ' '
    
    return st[:-1]