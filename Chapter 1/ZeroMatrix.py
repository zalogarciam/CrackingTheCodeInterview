def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    show_matrix = ""
    show_new_matrix = ""

    for i in range(rows):
        for j in range(cols):
            show_matrix += str(matrix[i][j]) + ' '
        show_matrix += '\n'
    print(show_matrix)

    loc_row = []
    loc_col = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                loc_row.append(i)
                loc_col.append(j)

    for row in loc_row:
        for i in range(cols):
            matrix[row][i] = 0

    for col in loc_col:
        for i in range(rows):
            matrix[i][col] = 0

    for i in range(rows):
        for j in range(cols):
            show_new_matrix += str(matrix[i][j]) + ' '
        show_new_matrix += '\n'
    print(show_new_matrix)

print(zero_matrix([[1, 1, 1, 1], [2, 0, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 0]]))
