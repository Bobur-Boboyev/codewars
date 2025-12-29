def sum_of_proper_divisors(n):
    total = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def buddy(start, limit):
    for n in range(start, limit + 1):
        m = sum_of_proper_divisors(n) - 1
        if m > n and sum_of_proper_divisors(m) == n + 1:
            return [n, m]
    return "Nothing"