def rotate_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    show_matrix = ""
    new_matrix = [[0] * cols] * rows
    show_new_matrix = ""

    for i in range(rows):
        for j in range(cols):
            show_matrix += str(matrix[i][j]) + ' '
        show_matrix += '\n'
    print(show_matrix)

    for i in range(rows):
        for j in range(cols):
            diff = (cols - 1) - i
            new_matrix[j][diff] = matrix[i][j]

    for i in range(rows):
        for j in range(cols):
            show_new_matrix += str(new_matrix[i][j]) + ' '
        show_new_matrix += '\n'
    print(show_new_matrix)

print(rotate_matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))
