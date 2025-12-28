from math import gcd
def reduce_fraction(fraction):
    num, denom = fraction
    common = gcd(num, denom)
    return (num // common, denom // common)