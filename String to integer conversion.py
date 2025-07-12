def my_parse_int(strn):
    s = strn.strip()
    if s.isdigit():
        return int(s)
    return 'NaN'