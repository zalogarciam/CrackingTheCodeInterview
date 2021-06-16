def perm_without_dups(S):
    if len(S) == 0:
        return [S]
    else:
        result = []
        for i in range(len(S)):
            current_char = S[i]
            rem = S[:i] + S[i + 1:]
            next_perms = perm_without_dups(rem)
            perms = [current_char + perm for perm in next_perms]
            result.extend(perms)
    return result

S = "aabc"
print(perm_without_dups(S))