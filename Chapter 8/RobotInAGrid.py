def robot_in_a_grid(maze, row , col, path):
    if maze[row][col] == 'R':
        return path
    if row >= 1 and col >= 0 and maze[row-1][col] is None and maze[row-1][col] != 'X':
        path.append((row-1, col))
        return robot_in_a_grid(maze, row-1, col, path)

    if row >= 0 and col >= 1 and maze[row][col-1] is None and maze[row][col-1] != 'X':
        path.append((row, col - 1))
        return robot_in_a_grid(maze, row, col-1, path)
    path.append((0, 0))
    return path


def robot_in_a_grid_v2(maze, row , col, path):
    if maze[row][col] == 'R':
        print(path)
        return path
    if row >= 0 and col >= 0 and maze[row][col] is None and maze[row][col] != 'X':
        path.append((row, col))

        return robot_in_a_grid_v2(maze, row-1, col, path) \
               and robot_in_a_grid_v2(maze, row, col-1, path)
    return path


maze = [['R', None, None, None, None],
        [None, 'X', None, None, None],
        [None, None, 'X', None, None],
        [None, 'X', None, None, None],
        [None, None, None, 'X', None]]

print(robot_in_a_grid(maze, 4, 4, []))
robot_in_a_grid_v2(maze, 4, 4, [])