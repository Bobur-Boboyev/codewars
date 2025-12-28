def rot(strng):
    ls = strng.split('\n')[::-1]
    empty_ls = list()
    
    for i in ls:
        s = ''
        for j in i[::-1]:
            s += j
        empty_ls.append(s)
    return '\n'.join(empty_ls)

def selfie_and_rot(strng):
    ls1 = [f"{i}{'.'*len(i)}" for i in strng.split('\n')]
    ls2 = [f"{'.'*len(i)}{i}" for i in rot(strng).split('\n')]
    
    l = ls1 + ls2
    return '\n'.join(l)
    

def oper(fct, s):
    return fct(s)