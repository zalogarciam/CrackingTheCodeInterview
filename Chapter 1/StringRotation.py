def string_rotation(a, b):
    c = b + b
    if a in c:
        return True
    else:
        return False

print(string_rotation('waterbottle', 'erbottlewat'))