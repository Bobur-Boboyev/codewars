def meeting(rooms, need):
    if need == 0:
        return "Game On"
    
    result = []
    
    for room in rooms:
        if need == 0:
            break
        
        people = len(room[0])
        chairs = room[1]
        free = max(chairs - people, 0)
        
        take = min(free, need)
        result.append(take)
        need -= take
    
    if need > 0:
        return "Not enough!"
    
    return result