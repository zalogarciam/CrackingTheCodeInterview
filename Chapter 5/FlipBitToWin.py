
def flip_bit_to_win(n):
    binary = bin(n)[2:]

    array_count = []
    flag_ones = False
    flag_zeros = False
    count_zeros = 0
    count_ones = 0

    for i in range(len(binary)):
        if binary[i] == '1':
            count_ones += 1
            flag_ones = True
            if flag_zeros:
                array_count.append((count_zeros, 0))
                count_zeros = 0
                flag_zeros = False

        elif binary[i] == '0':
            count_zeros += 1
            flag_zeros = True
            if flag_ones:
                array_count.append((count_ones, 1))
                count_ones = 0
                flag_ones = False

    if count_zeros > 0:
        array_count.append((count_zeros, 0))
    if count_ones > 0:
        array_count.append((count_ones, 1))
    maxi = 0
    for i in range(len(array_count) - 2):
        count = array_count[i][0]
        type = array_count[i][1]

        if type == 1 and (array_count[i + 1][1] == 0 and array_count[i + 1][0] == 1) \
                and (array_count[i + 2][1] == 1):
            suma = count + array_count[i + 1][0] + array_count[i + 2][0]
            maxi = max(maxi, suma)
    print(maxi)


def flipBit(num):
    currLen = 0
    prevLen = 0
    maxLen = 0
    while num > 0:
        if (num & 1) == 1:
            currLen += 1
        elif (num & 1) == 0:
            if (num & 2) == 0:
                prevLen = 0
            else:
                prevLen = currLen
            currLen = 0
        maxLen = max(prevLen + currLen, maxLen)
        num >>= 1
    return maxLen + 1

test = 124398
flip_bit_to_win(test)
print(flipBit(31))
print(flipBit(1775))
print(flipBit(86))
print(flipBit(124398))