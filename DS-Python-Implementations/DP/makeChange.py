def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cent in range(change+1):
        coinCount = cent
        newCoin = 1
        for j in [k for k in coinValueList if k <= cent]:
            if minCoins[cent - j] + 1 < coinCount:
                coinCount = minCoins[cent - j] + 1
                newCoin = j
        minCoins[cent] = coinCount
        coinsUsed[cent] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0] * (amnt+1)
    coinCount = [0] * (amnt+1)

    print("Making change for {} requires".format(amnt))
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), "coins")
    print("They are: ")
    printCoins(coinsUsed, amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()