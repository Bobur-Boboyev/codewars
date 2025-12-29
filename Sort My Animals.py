def sort_animals(lst: list) -> list:
    if not lst:
        return []

    result = lst.copy()
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            a, b = result[i], result[j]
            if a.number_of_legs > b.number_of_legs or (a.number_of_legs == b.number_of_legs and a.name > b.name):
                result[i], result[j] = result[j], result[i]
    return result