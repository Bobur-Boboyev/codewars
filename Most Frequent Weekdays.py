from datetime import date

def most_frequent_days(year):
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    
    first_day_index = date(year, 1, 1).weekday()
    
    leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    
    if leap:
        result = [days[first_day_index],
                  days[(first_day_index + 1) % 7]]
    else:
        result = [days[first_day_index]]
    
    return sorted(result, key=lambda d: days.index(d))