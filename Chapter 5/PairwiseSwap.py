def pairwise_swap(num):
    even = 0xaaaaaaaaaa
    odd = 0x5555555555
    even_clear = num & even
    odd_clear = num & odd
    return (even_clear >> 1) | (odd_clear << 1)

print(bin(pairwise_swap(29)))
