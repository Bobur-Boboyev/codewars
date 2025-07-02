def phone(strng, num):
    if num not in strng:
        return f"Error => Not found: {num}"
    if strng.count(num) > 1:
        return f"Error => Too many people: {num}"
    
    ls = strng.split('\n')
    for i in ls:
        if num in i:
            ls = i
            
    start = ls.find('<')+1
    end = ls.find('>')
    name = ls[start:end]
    
    ls = ls.replace(num, '').replace('<'+name+'>','')
    address = ''
    for a in ls:
        if a not in '+;!*/|$?_,:':
            address +=a
        else:
            address+=' '
    address = ' '.join(address.split())
    
    
    return f"Phone => {num}, Name => {name}, Address => {address}"