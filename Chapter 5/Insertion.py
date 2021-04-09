def insert(n, m, i, j):
    ones = ~0
    left = ones << (j + 1)
    right = (1 << i) - 1
    print(bin(left), bin(right))
    mask = left | right
    print(bin(mask))
    masked = n & mask
    m = m << i
    return masked | m

n = 0b10000000000
m = 0b10011
i = 2
j = 6
print(bin(insert(n, m, i, j)))