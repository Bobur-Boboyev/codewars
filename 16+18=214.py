def add(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    
    if len(num1) < len(num2):
        num1 = num1.rjust(len(num2), '0')
    elif len(num1) > len(num2):
        num2 = num2.rjust(len(num1), '0')
        
    result = ""
    
    for n1, n2 in zip(num1, num2):
        result += str(int(n1) + int(n2))
    
    return int(result)