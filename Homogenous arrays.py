def filter_homogenous(arrays):
    ls = []
    for i in arrays:
        s = 0
        integer = 0
        if i == []:
            continue
        for j in i:
            if type(j) is str:
                s+=1
            elif type(j) is int:
                integer+=1
        
        if len(i)==s or len(i)==integer:
            ls.append(i)
    return ls