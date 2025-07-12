def explode(arr):  
    is_num = [isinstance(i, (int, float)) for i in arr]

    if is_num == [True, True]:
        score = arr[0] + arr[1]
    elif is_num == [True, False]:
        score = arr[0]
    elif is_num == [False, True]:
        score = arr[1]
    else:
        return "Void!"

    return [arr] * score