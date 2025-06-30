def determine_time(arr):
    h = 24*60*60
    all_minutes = 0
    for i in arr:
        i = i.split(':')
        m= int(i[0])*60*60 + int(i[1])*60 + int(i[2])
        all_minutes += m
        
    return h >= all_minutes