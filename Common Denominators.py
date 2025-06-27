import math
def convert_fracts(lst):
    m = [i[1] for i in lst]
    if m == []:
        return []
    m = math.lcm(*m)
    k = []
    for i in lst:
        a = int(m/i[1])
        s = int(a*i[0])
        k.append([s, m])
    return k