
def boolean_evaluation(expr, result):
    if expr == "1":
        if result:
            return 1
        return 0
    if expr == "0":
        if not result:
            return 1
        return 0

    ways = 0

    for i in range(1, len(expr), 2):

        operator = expr[i]
        left = expr[0:i]
        right = expr[i + 1:]

        left_true = boolean_evaluation(left, True)
        left_false = boolean_evaluation(left, False)
        right_true = boolean_evaluation(right, True)
        right_false = boolean_evaluation(right, False)
        total_ways = (left_true + left_false) * (right_true + right_false)
        true_ways = 0

        if operator == "&":
            true_ways += left_true * right_true
        elif operator == "|":
            true_ways += (
                    (left_true * right_true)
                    + (left_true * right_false)
                    + (left_false * right_true)
            )
        elif operator == "^":
            true_ways += (left_true * right_false) + (left_false * right_true)

        if result:
            ways += true_ways
        else:
            ways += total_ways - true_ways

    return ways

print(boolean_evaluation("0&0&0&1^1|0", True))