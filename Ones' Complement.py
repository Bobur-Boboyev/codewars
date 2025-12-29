def ones_complement(binary_number):
    result = ['1' if i == '0' else '0' for i in binary_number]
    return ''.join(result)