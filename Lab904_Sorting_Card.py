array = [ '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K', 'A', '♣', '♦', '♥', '♠']

def insertionSort(Slist):
    encryp(Slist)
    wall = 1
    while wall <= len(Slist)-1:
        jim = Slist[wall]
        point = 0
        while point < wall:
            if jim[0] < Slist[point][0]:
                fii = Slist.index(Slist[point])
                Slist.remove(jim)
                Slist.insert(fii, jim)
                break
            elif jim[0] == Slist[point][0]:
                if jim[1] < Slist[point][1]:
                    fii = Slist.index(Slist[point])
                    Slist.remove(jim)
                    Slist.insert(fii, jim)
                    break
            point += 1
        wall += 1
    decryp(Slist)
    print(Slist)

def encryp(Slist):
    for i in range(len(Slist)):
        Slist[i] = [array.index(Slist[i][0:-1]), array.index(Slist[i][-1])]

def decryp(Slist):
    for i in range(len(Slist)):
        Slist[i] = array[Slist[i][0]]+array[Slist[i][1]]

def selectionSort(Slist):
    encryp(Slist)
    wall = 1
    while wall < len(Slist):
        num = [18, 18]
        for i in Slist[wall-1::]:
            if num[0] > i[0]:
                num = i
            elif num[0] == i[0]:
                if num[1] > i[1]:
                    num = i
        Slist.remove(num)
        Slist.insert(wall-1, num)
        wall += 1
    decryp(Slist)
    print(Slist)

def bubbleSort(Slist):
    encryp(Slist)
    while True:
        provit = Slist.copy()
        num = 0
        while num < len(Slist)-1:
            if Slist[num][0] > Slist[num+1][0]:
                Slist[num], Slist[num+1] = Slist[num+1], Slist[num]
            elif Slist[num][0] == Slist[num+1][0]:
                if Slist[num][1] > Slist[num+1][1]:
                    Slist[num], Slist[num+1] = Slist[num+1], Slist[num]
            num += 1
        if provit == Slist:
            decryp(Slist)
            print(Slist)
            break
print(ord('♣'), ord('♦'), ord('♠'), ord('♥'))
bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦', '10♦', '10♠'])
