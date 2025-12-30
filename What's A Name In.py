def name_in_str(strng: str, name: str) -> bool:
    strng = strng.lower()
    name = name.lower()
    i = 0

    for ch in strng:
        if i < len(name) and ch == name[i]:
            i += 1

    return i == len(name)