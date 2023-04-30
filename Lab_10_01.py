def coinExchange(amount, coinList):
    """ แลกเหรียญ """
    chest = coinList[0]*10+coinList[1]*5+coinList[2]*2+coinList[3]
    print("Amount:", amount)
    if amount > chest:
        return print("Coins are not enough.")
    num10 = amount//10;amount = amount%10
    if num10>coinList[0]:
        amount = amount+10*(num10-coinList[0])
        num10 = coinList[0]
    num5 = amount//5;amount = amount%5
    if num5>coinList[1]:
        amount = amount+5*(num5-coinList[1])
        num5 = coinList[1]
    num2 = amount//2;amount = amount%2
    if num2>coinList[2]:
        amount = amount+2*(num2-coinList[2])
        num2 = coinList[2]
    if amount > coinList[3]:
        return print("Coins are not enough.")
    print("Coin exchaneg result:", list((num10, num5, num2, amount)))
    return print("Number of coin:", sum(list((num10, num5, num2, amount))))

ccc = [10, 10, 10, 10]
coinExchange(249, ccc)