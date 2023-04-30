
class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getWeight(self):
        return self.weight
    def getCost(self):
        return self.price/self.weight

def knapsack(amount, itemList):
    """ pick """
    sortedList = sorted(itemList, key=lambda x:x.getWeight())
    base = amount+0
    amount = amount-sortedList[0].getWeight()
    dicBasket = {sortedList[0] : [sortedList[0].getPrice(), sortedList[0].getWeight(), sortedList[0].getName(), sortedList[0]]}
    #key คือ directory ส่วน value จะเป็นลิสต์ของ ราคา น้ำหนัก ชื่อ และ ไดเร็กทอรี่ของตัวเองอีกที
    #เพราะ ตอนแรกใช้เป็นค่า Costs หรือ directory เป็นkey แล้วเกิดปัญหาเรื่องการระบุว่าไอเทมตัวนั้นคือตัวไหนใน dicBasket
    #เลยให้มันมีทั้ง key และ value ที่เป็น directory
    for i in sortedList:
        posi = sorted(dicBasket.values(), key=lambda x:x[3].getCost())[0] # x:x[3].getCost เรียงโดยใช้ค่า Cost
        # posi จะเก็บค่าของ list ที่มีค่า Cost น้อยที่สุด
        lower = posi[3].getCost()
        # lower จะเก็บค่า Cost ที่น้อยที่สุดไว้
        if (i in dicBasket):
            # ไม่รับของซ้ำ
            continue
        elif (amount-i.getWeight()) < 0:
            if (i.getCost() >= lower) \
                and i.getWeight() >= posi[1]\
                    and amount+posi[1] >= i.getWeight():
                # การเปรียบเทียบคือ ถ้าค่า Cost มากกว่าหรือเท่ากัน และ ค่า Weight มากกว่าหรือเท่ากัน และ ถ้าจัดตะกร้าแล้วเหลือพื้นที่ให้ใส่มากพอ
                amount = amount+posi[1]
                dicBasket.pop(posi[3])
                dicBasket[i] = [i.getPrice(), i.getWeight(), i.getName(), i]
                amount = amount-i.getWeight()
        else:
            amount = amount-i.getWeight()
            dicBasket[i] = [i.getPrice(), i.getWeight(), i.getName(), i]
    print("Knapsack Size:", base, "kg")
    print("=========================================")
    jam = 0
    for j in dicBasket:
        jam = jam+j.getPrice()
        print(j.getName(), "->", j.getWeight(), "kg", "->", j.getPrice(), "THB")
    print("Total:", jam, "THB")

# Not Greedy some TestCase
item1 = Item('tablet', 7000, 0.5)
item2 = Item('perfume', 6000, 0.5)
item3 = Item('guitar', 9000, 1)
item4 = Item('air purifier', 9000, 2)
item5= Item('watch', 8000, 0.5)
itemList = [item1, item2, item3,
item4, item5]
knapsack(3, itemList)