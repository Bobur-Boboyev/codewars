from collections import Counter
def mix(s1, s2):
    c1 = Counter(c for c in s1 if c.islower())
    c2 = Counter(c for c in s2 if c.islower())
    
    res = []
    for char in set(c1.keys()) | set(c2.keys()):
        count1, count2 = c1[char], c2[char]
        max_count = max(count1, count2)
        
        if max_count > 1:
            if count1 > count2:
                res.append(f"1:{char * max_count}")
            elif count2 > count1:
                res.append(f"2:{char * max_count}")
            else:
                res.append(f"=:{char * max_count}")
    
    res.sort(key=lambda x: (-len(x), x[0], x[2]))
    
    return "/".join(res)