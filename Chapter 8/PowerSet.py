def add_element(list_of_lists, n):
    for list in list_of_lists:
        list.append(n)
    return list_of_lists

def power_set(n):
    if n == 0:
        return []
    if n == 1:
        return [[], [n]]
    if n == 2:
        return [[], [n-1], [n], [n-1, n]]
    if n >= 3:
        return power_set(n-1) + add_element(power_set(n-1), n)



print((power_set(5)))


from itertools import combinations
def power_set_iter(n):
    listrep = list(n)
    subsets = []
    for i in range(2 ** len(listrep)):
        subset = []
        for k in range(len(listrep)):
            if i & 1 << k:
                subset.append(listrep[k])
        subsets.append(subset)
    return subsets


subsets = power_set_iter([1, 2, 3])
print(subsets)
print(len(subsets))


print((power_set_iter(3)))