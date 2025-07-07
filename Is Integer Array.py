def is_int_array(arr):
    if type(arr) == bool or type(arr)==int or type(arr)==float or type(arr) == str or arr ==None or type(arr)==dict or type(arr)==set:
        return False
    if arr == []:
        return True
    
    for i in arr:
        if type(i) == str:
            return False
        if type(i) == float:
            if i%1>0:
                return False
        if i == None:
            return False
    return True