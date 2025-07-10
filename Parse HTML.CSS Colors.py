def parse_html_color(color):
    color = color.lower()
    if color in PRESET_COLORS:
        color = PRESET_COLORS[color]
    
    if len(color) == 4:
        r = int(color[1] * 2, 16)
        g = int(color[2] * 2, 16)
        b = int(color[3] * 2, 16)
    elif len(color) == 7:
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:], 16)
    return {'r':r,'g':g,'b':b}