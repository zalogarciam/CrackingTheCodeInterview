def conversion(n1, n2):
    n = n1 ^ n2
    count = 0
    while n != 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count

print(conversion(29, 15))
