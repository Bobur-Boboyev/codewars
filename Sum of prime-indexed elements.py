def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def total(arr):
    prime_numbers = []
    
    for i in range(len(arr)):
        if isPrime(i):
            prime_numbers.append(i)
    
    sum_of_prime_numbers = sum(map(lambda i: arr[i], prime_numbers))
    
    return sum_of_prime_numbers