def scoreboard(st):
    ls = []
    numbers = {'nil':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for i in st.split():
        if i in numbers:
            ls.append(numbers[i])
    
    return ls