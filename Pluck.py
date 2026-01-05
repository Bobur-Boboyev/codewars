def pluck(objs: list[dict[str: int]], name: str)-> list: 
    ls = []
    
    for i in objs:
        ls.append(i.get(name, None))
    
    return ls