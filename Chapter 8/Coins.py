memo = {}
def coins_util(amount, i, coins):

    global memo
    key = (i, amount)
    if key in memo:
        return memo[key]

    if i == 0:
        return 1
    elif amount < 0:
        return 0

    top = 0
    if amount - coins[i] >= 0:
        top = coins_util(amount - coins[i], i, coins)
    down = coins_util(amount, i - 1, coins)

    memo[key] = top + down
    return top + down

def coins(amount):
    coins = [1, 5 , 10 ,25]
    return coins_util(amount, len(coins) - 1, coins)

print(coins(10))