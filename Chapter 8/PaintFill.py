
grid = [
            ['white', 'white','red','red'],
            ['white', 'white','white','white'],
            ['white', 'white','white','white'],
            ['blue', 'blue','white','white'],
            ['blue', 'blue','white','white'],
        ]


def paint_fill(grid, row, col, color):
    target_color = grid[row][col]
    paint_fill_helper(grid, row, col, target_color, color)


def paint_fill_helper(grid, row, col, color_from, color_to):
    if not coords_in_bounds(grid, row, col):
        return

    if grid[row][col] == color_from:
        grid[row][col] = color_to
        paint_fill_helper(grid, row - 1, col, color_from, color_to)
        paint_fill_helper(grid, row + 1, col, color_from, color_to)
        paint_fill_helper(grid, row, col - 1, color_from, color_to)
        paint_fill_helper(grid, row, col + 1, color_from, color_to)


def coords_in_bounds(grid, row, col):
    row_in_bounds = row < len(grid) and row >= 0
    col_in_bounds = col < len(grid[0]) and col >= 0
    return row_in_bounds and col_in_bounds


def get_neighbours(grid, pop_item):
    row = pop_item[0]
    col = pop_item[1]
    neighbours = []
    len_row = len(grid) - 1
    len_col = len(grid[0]) - 1

    if row > 1:
        neighbours.append((row - 1, col))
    if row < len_row:
        neighbours.append((row + 1, col))
    if col > 1:
        neighbours.append((row, col - 1))
    if col < len_col:
        neighbours.append((row, col + 1))

    return neighbours

def paint_fill_dfs(grid, row, col, color):

    stack = [(row, col)]
    visited = []

    while len(stack) > 0:
        pop_item = stack.pop(-1)
        if pop_item not in visited:
            visited.append(pop_item)
            p_row = pop_item[0]
            p_col = pop_item[1]
            if grid[p_row][p_col] == "white":
                grid[p_row][p_col] = color
        neighbours = get_neighbours(grid, pop_item)
        for neighbour in neighbours:
            if neighbour not in visited:
                stack.append(neighbour)
    return grid


print(paint_fill(grid, 0, 0, 'blue'))
for i in grid:
    print(i)

grid_returned = (paint_fill_dfs(grid,0 ,0 , 'blue'))
for i in grid_returned:
    print(i)
