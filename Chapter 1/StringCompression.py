def string_compression(string):
    res = ""
    prev = string[0]
    count = 1
    for i in range(1, len(string)):
        if prev == string[i]:
            count += 1
        else:
            res += prev + str(count)
            count = 1
        prev = string[i]
    res += prev + str(count)
    return res if len(res) < len(string) else string

print(string_compression("aabcccccaaa"))
