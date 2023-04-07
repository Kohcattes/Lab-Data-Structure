def insertionSort(Slist):
    wall = 1
    while wall <= len(Slist)-1:
        jim = Slist[wall]
        point = 0
        while point < wall:
            if jim <= Slist[point]:
                fii = Slist.index(Slist[point])
                Slist.remove(jim)
                Slist.insert(fii, jim)
                break
            point += 1
        print(Slist)
        wall += 1

def selectionSort(Slist):
    wall = 1
    while wall < len(Slist):
        num = min(Slist[wall-1::])
        Slist.remove(num)
        Slist.insert(wall-1, num)
        print(Slist)
        wall += 1

def bubbleSort(Slist):
    while True:
        provit = Slist.copy()
        num = 0
        while num < len(Slist)-1:
            if Slist[num] > Slist[num+1]:
                Slist[num], Slist[num+1] = Slist[num+1], Slist[num]
            num += 1
        print(Slist)
        if provit == Slist:
            break

ohoh = [23, 78, 45, 8, 32, 56]
#selectionSort(ohoh)
print("-------------------------")
bubbleSort(ohoh)
