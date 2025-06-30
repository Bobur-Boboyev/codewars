def dominator(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for k,v in d.items():
        if v>len(arr)//2:
            return k
    return -1