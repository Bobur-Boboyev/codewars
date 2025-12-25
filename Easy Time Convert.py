def time_convert(num):
    if num <= 0:
        return "00:00"
    
    hour = str(num // 60)
    minute = str(num % 60)
    
    hour = hour.rjust(2, '0')
    min = minute.rjust(2, '0')
    
    return f"{hour}:{min}"