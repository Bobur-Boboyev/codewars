def avg_array(arr):
    rows = len(arr)
    cols = len(arr[0])
    result = []

    for i in range(cols):
        total = 0
        for j in range(rows):
            total += arr[j][i]
        result.append(total / rows)

    return result
