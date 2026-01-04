def pluck(objs, name): 
    ls = []
    
    for i in objs:
        ls.append(i.get(name, None))
    
    return ls