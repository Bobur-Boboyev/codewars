from collections import defaultdict
import re

def simplify(poly):
    counter = defaultdict(int)
    for term in re.findall(r'[+-]?\d*[a-z]+', poly.replace(' ', '')):
        m = re.match(r'([+-]?\d*)([a-z]+)', term)
        c, v = m.groups()
        coeff = int(c) if c not in ('', '+', '-') else 1 if c in ('', '+') else -1
        counter[''.join(sorted(v))] += coeff
    
    items = sorted(((v,k) for k,v in counter.items() if v != 0), key=lambda x: (len(x[1]), x[1]))
    
    result = ''
    for i, (coeff, var) in enumerate(items):
        if coeff > 0 and i > 0:
            result += '+'
        if abs(coeff) != 1:
            result += str(coeff)
        elif coeff == -1:
            result += '-'
        elif coeff == 1 and i == 0:
            result += ''
        result += var
    return result