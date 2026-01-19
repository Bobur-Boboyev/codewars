def group(arr):
    d = {}
    for i in arr:
        d[i] = arr.count(i)
        
    result = list(map(lambda i: [i[0]] * i[1], d.items()))
    
    return result