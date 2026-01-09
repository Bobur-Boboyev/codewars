def sol_equa(n):
    result = []
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            b = n // a
            if (a + b) % 2 == 0 and (b - a) % 4 == 0:
                x = (a + b) // 2
                y = (b - a) // 4
                result.append([x, y])
    result.sort(reverse=True, key=lambda pair: pair[0])
    return result