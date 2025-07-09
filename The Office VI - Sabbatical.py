def sabb(s, val, happiness):
    v = 'sabbatical'
    d = []
    for i in s:
        if i in v:
            d.append(1)
    s = sum(d)+val+happiness
    if s > 22:
        return "Sabbatical! Boom!"
    else:
        return "Back to your desk, boy."
