def closest(strng):
    if not strng:
        return []

    numbers = strng.split()
    nums_info = []
    for idx, num in enumerate(numbers):
        weight = sum(int(d) for d in num)
        nums_info.append([weight, idx, int(num)])

    nums_info.sort(key=lambda x: (x[0], x[1]))

    min_diff = float('inf')
    result = []
    for i in range(len(nums_info) - 1):
        w1, idx1, n1 = nums_info[i]
        w2, idx2, n2 = nums_info[i+1]
        diff = abs(w2 - w1)
        if diff < min_diff:
            min_diff = diff
            result = [[w1, idx1, n1], [w2, idx2, n2]]

    return result