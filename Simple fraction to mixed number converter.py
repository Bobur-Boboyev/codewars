import math
def mixed_fraction(s):
    a, b = [int(i) for i in s.split('/')]
    
    if b == 0:
        raise ZeroDivisionError('error!')
    
    if a == 0:
        return '0'
    
    sign = '-' if (a < 0) ^ (b < 0) else ''

    a, b = abs(a), abs(b)
    
    whole = a // b
    rest = a - (whole * b)
    
    ekub = math.gcd(a, b)
    rest //= ekub
    b //= ekub
    
    if whole == 0:
        return f"{sign}{rest}/{b}"
    
    if rest == 0:
        return sign + str(whole)

    return f"{sign}{whole} {rest}/{b}"