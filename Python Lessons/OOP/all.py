class item:
    all2 = []
    rate = 0.8    # price after 20 % discount
    def __init__(self,name,price,quantity):    #self is for item1,item2,iteem3 specifically
        self.name = name
        self.price = price
        self.quantity = quantity
        item.all2.append(self)

        # assert basically check the conditions true or not...if not it gives assertionerror....
        assert price >= 0 , f"given price is not greater than zero"
        assert quantity >= 0  , f"given price is not greater than zero"
    
    def apply_discount(self):
        self.priced = self.price * self.rate
        return self.priced

item1 = item("ice",20,5)
item2 = item("WATER", 30, 5)
item3 = item("cooldrink", 25 , 3)

#printing item details         # print(item1.name)
                 #  print(item1.price)
                # print(item1.quantity)
item1.rate = 0.7  # discount rate 70% for item1
item3.rate = 0.75  # discount rate 70% for item1

# print(item.rate)  --- this is hw we can print rate 
#print(item1.rate)   --- it will give 0.8 output even if its not in __init__ method 

addition= [item1.price , item2.price , item3.price]         #item prices in list
total = [item1.quantity , item2.quantity , item3.quantity]   # quntities of items in list format
discounted = [item1.apply_discount() , item2.apply_discount() , item3.apply_discount()]   #item discounted price in list format 

print(f"price of {item1.name},{item2.name},{item3.name} is {sum(addition)} and the quantites are {sum(total)} and discounted price is {sum(discounted)}") 

# print(f"discounted price of item1 is {item1.apply_discount()} at {item1.rate *100}% rate   original price of item1 is {item1.price}")
# print(f"discounted price of item2 is {item2.apply_discount()} at {item2.rate *100}% rate   original price of item2 is {item2.price}")
# print(f"discounted price of item3 is {item3.apply_discount()} at {item3.rate * 100}% rate  original price of item3 is {item3.price}")
# print(item.all2)
for instance in item.all2:
    print(instance.name, end=" ")
    print(instance.price, end=" ")
    print(instance.quantity)
