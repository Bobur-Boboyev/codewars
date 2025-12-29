def to_acronym(inp):
    s = ''
    for i in inp.split():
        s += i[0]
    
    return s.upper()