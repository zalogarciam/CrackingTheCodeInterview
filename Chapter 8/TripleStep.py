
def triple_step(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

def triple_step_memo(n, memo):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        result = triple_step_memo(n-1, memo) + triple_step_memo(n-2, memo) + triple_step_memo(n-3, memo)
    if result not in memo:
        memo[n] = result
    return result

import time
start_time = time.time()
print(triple_step(30))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(triple_step_memo(30, {}))
print("--- %s seconds ---" % (time.time() - start_time))
