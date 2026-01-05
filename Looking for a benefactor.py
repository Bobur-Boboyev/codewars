import math

def new_avg(arr, newavg):
    n = len(arr)
    total = sum(arr)
    next_donation = math.ceil(newavg * (n + 1) - total)
    if next_donation <= 0:
        raise ValueError("Error")
    return next_donation