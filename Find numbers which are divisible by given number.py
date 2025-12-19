def divisible_by(numbers, divisor):
    ls = []
    for i in numbers:
        if i % divisor == 0:
            ls.append(i)
    
    return ls