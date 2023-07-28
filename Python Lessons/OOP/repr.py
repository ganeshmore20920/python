class item:
    all = []
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        item.all.append(self)
    def __repr__(self):
        return f"item({self.name},{self.price},{self.quantity})"
item1 = ("Apple" , 40 ,2)
item2 = ("Banana" , 60 , 4)
item3 = ("Pineapple" , 100 , 8)
item4 = ("Grapes" ,50 , 5)
for instance in all:
    print(all.name)