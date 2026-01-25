def word_to_bin(word):
    ls = list()
    
    for i in word:
        a = ord(i)
        b = bin(a).replace('b', '')
        ls.append(b)
    
    return ls