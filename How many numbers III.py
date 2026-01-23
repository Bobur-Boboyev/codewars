def find_all(sum_dig, digs):
    result = []

    def dfs(pos, last_digit, remaining_sum, current):
        if pos == digs:
            if remaining_sum == 0:
                result.append(int(''.join(map(str, current))))
            return

        for d in range(last_digit, 10):
            if remaining_sum - d < 0:
                break
            dfs(pos + 1, d, remaining_sum - d, current + [d])

    dfs(0, 1, sum_dig, [])

    if not result:
        return []

    return [len(result), result[0], result[-1]]