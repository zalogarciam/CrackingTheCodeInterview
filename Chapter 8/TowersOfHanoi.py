def hanoi_towers(n, source, buffer, destination):
    if n == 0:
        return
    hanoi_towers(n - 1, source, destination, buffer)
    print("Move disk", n, "from source", source, "to destination", destination)
    hanoi_towers(n - 1, buffer, source, destination)

n = 3
hanoi_towers(n, '1', '2', '3')