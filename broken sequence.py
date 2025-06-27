def find_missing_number(sequence):
    if sequence.strip() == '':
        return 0

    numbers = []
    for item in sequence.split():
        try:
            numbers.append(int(item))
        except ValueError:
            return 1

    for i in range(1, max(numbers) + 1):
        if i not in numbers:
            return i

    return 0