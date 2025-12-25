def count_deaf_rats(town):
    piper = town.index("P")
    
    left = town[:piper].replace(" ", '')
    right = town[piper+1:].replace(" ", '')
    
    c = 0
    
    i = 0
    while i < len(left):
        if left[i:i+2] == "O~":
            c += 1
        i += 2
    
    i = 0
    while i < len(right):
        if right[i:i+2] == "~O":
            c += 1
        i += 2
    
    return c