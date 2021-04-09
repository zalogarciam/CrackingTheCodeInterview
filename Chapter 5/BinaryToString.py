def binary_to_string(n):
    result = '0.'
    while n != 1 and len(result) <= 32:
        n *= 2
        if n >= 1:
            if n == 1:
                result += '1'
                break
            result += '1'
            n -= 1
        else:
            result += '0'
    if len(result) == 32:
        print("ERROR")
    else:
        print(result)

binary_to_string(0.625)
