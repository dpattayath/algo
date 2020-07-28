
"""
memoization approach (top down)
"""
def coin_change_recursive(coins, money, index, memo):
    if money == 0:
        return 1
    if index >= len(coins):
        return 0

    key = str(money) + '-' + str(index)
    if memo.get(key, 0) != 0:
        return memo.get(key)

    amount_with_coin = 0
    ways = 0
    while amount_with_coin <= money:
        remaining = money - amount_with_coin
        ways += coin_change_recursive(coins, remaining, index+1, memo)
        amount_with_coin += coins[index]
    memo[key] = ways
    return ways

"""
tabulation approach (bottom up)
"""
def coin_change_iterative(coins, money):
    combinations = [0] * (money + 1)
    combinations[0] = 1

    for coin in coins:
        for i in range(len(combinations)):
            if i >= coin:
                combinations[i] += combinations[i - coin]

    return combinations[money]

if __name__ == "__main__":
    print(coin_change_recursive([50, 25, 10, 5, 1], 79, 0, {}))
    print(coin_change_recursive([25, 10, 5, 1], 27, 0, {}))
    print(coin_change_recursive([1, 2, 5], 5, 0, {}))
    print(coin_change_recursive([1, 2, 5], 12, 0, {}))

    print(coin_change_iterative([50, 25, 10, 5, 1], 79))
    print(coin_change_iterative([25, 10, 5, 1], 27))
    print(coin_change_iterative([1, 2, 5], 5))
    print(coin_change_iterative([1, 2, 5], 12))
