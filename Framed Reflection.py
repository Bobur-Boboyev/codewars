def mirror(text):
    words = text.split()
    
    space = len(max(words, key=len))
    
    border = '*' * (space + 4)
    
    lines = [border]
    
    for word in words:
        line = '* ' + word[::-1] + ' ' * (space - len(word)) + ' *'
        lines.append(line)
    
    lines.append(border)
    
    return '\n'.join(lines)