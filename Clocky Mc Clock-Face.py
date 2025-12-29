def what_time_is_it(angle):
    total_hours = angle / 30
    hours = int(total_hours) % 12
    if hours == 0:
        hours = 12
    minutes = int((total_hours - int(total_hours)) * 60)
    return f"{hours:02d}:{minutes:02d}"