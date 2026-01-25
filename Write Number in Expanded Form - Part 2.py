def expanded_form(num):
    num = str(num)
    result = []

    if '.' in num:
        integer, decimal = num.split('.')
    else:
        integer, decimal = num, ''
        
    for i, d in enumerate(integer):
        if d != '0':
            result.append(d + '0' * (len(integer) - i - 1))

    for i, d in enumerate(decimal):
        if d != '0':
            result.append(f"{d}/{10 ** (i + 1)}")

    return " + ".join(result)