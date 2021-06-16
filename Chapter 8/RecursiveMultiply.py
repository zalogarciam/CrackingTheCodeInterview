def recursive_multiply_(a, b, result):
    if b == 0:
        return result
    return recursive_multiply_(a, b - 1, result + a)

def recursive_multiply(a, b):
    return recursive_multiply_(a, b, 0)


def recursive_multiply_v_(a, b, count, result):
    if count == 0:
        if b % 2 == 1:
            return result * 2 + a
        else:
            return result * 2
    return recursive_multiply_v_(a, b, count - 1, result + a)

def recursive_multiply_v(a, b):
    if a >= b:
        return recursive_multiply_v_(a, b, b // 2, 0)
    else:
        return recursive_multiply_v_(b, a, a // 2, 0)



print(recursive_multiply(4, 7))
print(recursive_multiply_v(7, 6))
print(recursive_multiply_v(6, 7))
print(recursive_multiply_v(6, 5))
print(recursive_multiply_v(8, 6))
print(recursive_multiply_v(6, 8))
print(recursive_multiply_v(5, 3))
