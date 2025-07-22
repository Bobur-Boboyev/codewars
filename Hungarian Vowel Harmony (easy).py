def dative(word):
    a = 'eéiíöőüű'
    b = 'aáoóuú'
    for ch in reversed(word):
        if ch in a:
            return word + 'nek'
        elif ch in b:
            return word + 'nak'
    return word