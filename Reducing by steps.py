import math
def gcdi(x,y):
    return math.gcd(abs(x), abs(y))
def lcmu(a, b):
    return abs(a * b) // math.gcd(abs(a), abs(b))
def som(a, b):
    return a+b
def maxi(a, b):
    if a > b:
        return a
    else:
        return b
def mini(a, b):
    if a < b:
        return a
    else:
        return b
def oper_array(fct, arr, init): 
    ls = []
    a = init
    for i in arr:
        a = fct(i, a)
        ls.append(a)
    return ls