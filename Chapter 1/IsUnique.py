def is_unique(string):
    if len(string) > len(set(string)):
        return False
    else:
        return True

print(is_unique("abcde"))
print(is_unique("abccdee"))