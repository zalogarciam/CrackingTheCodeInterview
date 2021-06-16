def magic_index(arr, index):
    if index == arr[index]:
        return arr[index]
    return magic_index(arr, index - 1)

def magic_index_v2(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magic_index_v2(arr, start, mid -1)
    else:
        return magic_index_v2(arr, mid + 1, end)

arr = [-20, -8, -4, -1, 0, 5, 10, 11, 19]
arr2 = [-20, -8, -4, -1, 0, 9, 10, 11, 19]

print(magic_index(arr, len(arr) - 1))
print(magic_index_v2(arr, 0, len(arr) - 1))
print(magic_index_v2(arr2, 0,  len(arr2) - 1))


arr = [-10, -5, 2, 2, 2, 3, 4, 7 , 9, 12, 13]
def magic_index_rem(arr, start, end):
    mid = (start + end) // 2
    if end < start:
        return -1
    if mid == arr[mid]:
        return mid

    left_index = min(mid - 1, arr[mid])
    print('Left index', left_index, mid)

    left = magic_index_rem(arr, start, left_index)
    print('Left', left, mid)
    if left >= 0:
        return left
    right_index = max(mid + 1, arr[mid])
    print('Right index', right_index, mid)

    right = magic_index_rem(arr, right_index, end)
    print('Right', right, mid)

    return right


print(magic_index_rem(arr, 0, len(arr)))