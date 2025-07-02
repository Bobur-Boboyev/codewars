def highest_rank(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ls = sorted(d.items(), key=lambda x: x[1], reverse=True)
    f = filter(lambda x: ls[0][1]==x[1], ls)
    ls = list(f)
    return sorted(ls, reverse=True)[0][0]