import sys

""" A function to calculate no. of combinations of coins possible for given coins and a given amount."""


def coin_change_combinations(coins: list, amount: int)->int:
    table = [0] * (amount+1)

    table[0] = 1
    for coin in coins:
        for j in range(coin, amount+1):
            table[j] += table[j-coin]
    return table[amount]


""" A function to calculate minimum no. of coins in change for given coins and amount """


def coin_change_min(coins: list, amount: int)->int:
    table = [sys.maxsize] * (amount+1)

    table[0] = 0
    for coin in coins:
        for j in range(coin, amount+1):
            table[j] = min(table[j-coin]+1, table[j])

    return table[amount]


if __name__ == '__main__':
    coins = [1, 3, 5]
    amount = 8
    print(coin_change_combinations(coins, amount))
    print(coin_change_min(coins, amount))