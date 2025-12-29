def max_product(arr):
    a = max(arr)
    arr.remove(a)
    b = max(arr)
    return a * b