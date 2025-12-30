def int_diff(arr, n):
    if n < 0:
        return 0

    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == n:
                count += 1
    return count