def solution(first, second):
    
    ls = []
    
    while True:
        ls.append((first, second))
        num = first
        first = second - first
        second = num
        
        if first < 0:
            break
            
    return ls[:-1][-1]