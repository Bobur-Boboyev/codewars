def complete_series(seq): 
    for i in seq:
        if seq.count(i) > 1:
            return [0]
    return list(range(max(seq)+1))