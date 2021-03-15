def one_away(a, b):
    letters = {}
    for i in a:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    for i in b:
        if i not in letters:
            letters[i] = -1
        else:
            letters[i] -= 1
    count = 0
    for letter in letters:
        if letters[letter] > 0:
            count += 1
        if letters[letter] < 0:
            count += 1
        if count > 2:
            return False

    return True

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
print(one_away("pale", "bakes"))