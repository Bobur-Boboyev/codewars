def stock_list(stocklist, categories):
    
    if not stocklist or not categories:
        return ''
    
    ls = []
    
    for i in categories:
        count = 0
        for j in stocklist:
            if i == j[0].upper():
                count += int(j.split()[-1])
        ls.append(f"({i} : {count})")
        
    result = " - ".join(ls)
    
    return result