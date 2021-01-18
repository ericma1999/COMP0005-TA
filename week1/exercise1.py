def findCoins(coins, target):
    n = len(coins)

    i = n - 1

    counter = 0

    while i >= 0:

        while (target >= coins[i]):
            target -= coins[i]
            counter+= 1
        i -= 1

    return counter



# N^2 Complexity
print(findCoins([1,5,10,20,50], 150))