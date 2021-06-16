def parens(s, left, right, n, result):
    if left == n and right == n:
        result.append(s)

    if left < n:
        parens(s + '(', left + 1, right, n, result)

    if right < left:
        parens(s + ')', left, right + 1, n, result)
    return result

n = 3
print(parens('', 0, 0, n, []))