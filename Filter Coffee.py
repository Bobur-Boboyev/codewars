def search(budget, prices):
    ls = []
    
    if len(prices) == 0:
        return ''
    
    for i in prices:
        if i <= budget:
            ls.append(i)
    
    result = ','.join(map(str, sorted(ls)))
    
    return result