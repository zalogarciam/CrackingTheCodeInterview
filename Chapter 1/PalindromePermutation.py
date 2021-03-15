def palindrome_permutation(string):
    string = string.lower()
    string = string.replace(' ', '')
    letters = {}
    for i in string:
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1

    count_odd = 0
    for letter in letters:
        if letters[letter] % 2 == 0:
            continue
        else:
            count_odd += 1
        if count_odd > 1:
            return False
    return True

print(palindrome_permutation("Tact Coa"))
