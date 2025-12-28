from preloaded import greek_alphabet


def greek_comparator(lhs, rhs):
    a = greek_alphabet.index(lhs)
    b = greek_alphabet.index(rhs)
    
    return a - b