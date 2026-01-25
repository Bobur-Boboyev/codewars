from random import randint

def random_case(x):
    s = ''
    
    for i in x:
        r = randint(0,1)
        
        if r:
            s += i.upper()
        else:
            s += i.lower()
    
    return s    