def all_non_consecutive(arr):
    ls = []
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            ls.append({'i': i + 1, 'n': arr[i + 1]})
    return ls