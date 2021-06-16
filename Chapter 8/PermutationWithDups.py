
def permute(input):
    count_map = {}
    for ch in input:
        if ch in count_map.keys():
            count_map[ch] = count_map[ch] + 1
        else:
            count_map[ch] = 1

    keys = sorted(count_map)
    str = ""
    count = []
    for key in keys:
        str += key
        count.append(count_map[key])

    result = [" " for x in range(len(input))]
    permute_util(str, count, result, 0)

def permute_util(str, count, result, i):
    if i == len(result):
        print("".join(result))
        return

    for i in range(len(str)):
        if count[i] == 0:
            continue
        result[i] = str[i]
        count[i] -= 1
        permute_util(str, count, result, i + 1)
        count[i] += 1

permute(S)

S = "abc"
permute(S)