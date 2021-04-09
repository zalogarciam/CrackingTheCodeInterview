def draw_line(screen, width, x1, x2, y):

    index_start = y * width + x1
    line_width = x2 - x1 + 1
    for i in range(line_width):
        screen[index_start + i] = 255
    return screen

screen = []
blank_byte = 0
filled_byte = 255
width = 6
height = 8

for i in range(width * height):
    screen.append(blank_byte)
result = draw_line(screen, width, 2, 4, 2)
print(result)
