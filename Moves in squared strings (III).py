def rot_90_clock(strng):
    ls = strng.split('\n') 
    l = []
    for i in range(len(ls)):
        s=''
        for j in ls[::-1]:
            s += j[i]
        l.append(s)
    return '\n'.join(l)

def diag_1_sym(strng):
    ls = strng.split('\n') 
    l = []
    for i in range(len(ls)):
        s=''
        for j in ls:
            s += j[i]
        l.append(s)
    return '\n'.join(l)
def selfie_and_diag1(strng):
    ls = strng.split('\n')
    l = []
    for i in range(len(ls)):
        s = ''
        for j in ls:
            s += j[i]
        l.append(s)
    lst = []
    for k in range(len(ls)):
        st = ''
        st += ls[k]+'|'+l[k]
        lst.append(st)
    return '\n'.join(lst)

def oper(fct, s):
    return fct(s)