import math
def wallpaper(l, w, h):
    if l == 0 or w == 0 or h==0:
        return 'zero'
    
    r = 10 * 0.52
    wall = (2 * h * (l+w)) * 1.15
    rr = wall/r
    return numbers[math.ceil(rr)]