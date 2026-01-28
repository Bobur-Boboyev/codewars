def more_zeros(s):
    ascii_codes = map(lambda x: ord(x), s)
    binary = map(lambda x: bin(x)[2:], ascii_codes)
    ls = map(lambda x: x.count('0') > x.count('1'), binary)
    result =  []
    for ind, item in enumerate(ls):
        if item and s[ind] not in result:
            result.append(s[ind])
    return result