
def is_valid(columns, row1, col1):
    if col1 in columns:
        return False

    for row2, col2 in enumerate(columns):
        if col2 is not None:
            if abs(col1 - col2) == abs(row1 - row2):
                return False

    return True

def eight_queens_util(column, row, result, n):
    if row == n:
        result.append(column)
        return

    for col in range(0, n):
        if is_valid(column, row, col):
            cols_copy = column[:]
            cols_copy[row] = col
            eight_queens_util(cols_copy, row + 1, result, n)

def eight_queens(n):
    result = []
    columns = [None] * n
    eight_queens_util(columns, 0, result, n)
    return result

print(eight_queens(4))
