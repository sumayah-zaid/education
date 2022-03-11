import math
class Grocery:
    def __init__(self):
        self.items = {
                'Banana': {'price': 4,   'stock': 6, 'code':1 },
                'Apple ':  {'price': 2,   'stock': 3,'code':2 },
                'Orange': {'price': 5, 'stock': 32,'code':3},
                'Cherry':   {'price': 3,   'stock': 15,'code':4},
                'Grapes':   {'price': 5,   'stock': 10,'code':5},
            }
    
    def print_items(self):
        counter = 1
        for key in self.items:
            print(f"{counter}- {key}")
            counter += 1



class Bill:
    def __init__(self, grocery):
        self.grocery = grocery # Contain Dictionary
        self.price = []
        self.total = []
        self.products = []
        self.quantity = []
    
    def buy(self, quantity, code):
        for key in self.grocery.items:
            if self.grocery.items[key]['code'] == code: # if the code provided is == to the items code
                if self.grocery.items[key]['stock'] < quantity: # if the quantity less than the stock
                    print("Out of stock")
                    total = sum(self.price);
                else:
                    self.grocery.items[key]['stock'] -= quantity # Subtract the quantity of the stock
                    #print the items info
                    print (key, "| price:", self.grocery.items[key]['price'], "| Stock:", self.grocery.items[key]['stock'], "| Barcode:", self.grocery.items[key]['code'])
                   
                    self.price.append(self.grocery.items[key]['price'])
                    self.total.append(self.grocery.items[key]['price'] * quantity) # append the (price * quantity) to the self.price array
                    total = sum(self.total); # Sum all the prices to calculate the total
                    self.quantity.append(quantity)
                    self.products.append(key) # append the list of product to self.products array
                    
        print("..............................................")
        return total


class Stock:
    def __init__(self, grocery):
        self.grocery = grocery

        for key in grocery.items:
            print(key, "-----", self.grocery.items[key]['stock'])
            




store = Grocery() #contain the Dictionary
bill1 = Bill(store)



finish = True
while finish:
    print("")
    print("1. Check for stuck")
    print("2. Buy items")

    q1 = int(input("Please enter the number of the action: "))

    if q1 == 1:
        bill2 = Stock(store) #check for stock
    elif q1 == 2:
        store.print_items()
        item_number = int(input("Please Enter the number of the item: "))
        quantity = int(input("Please enter the quantity needed: "))
        total = bill1.buy(quantity, item_number)

        exit_statment = input("Do you need somthing else (y/n): ")
        if exit_statment == "n":
            finish = False

    

print("")
print("|----------------------------------|")
print("|  Item   |   Price  |   Quantity  |")
print("|---------|----------|-------------|")

for i in range (len(bill1.products)):
    print(f"|  {bill1.products[i]} |     {bill1.price[i]}    |      {bill1.quantity[i]}      |")
    print("|---------|----------|-------------|")

print("|----------------------------------|")
print("|                                  |")
print("|        The total is:", total, "         |")
print("|                                  |")
print("|----------------------------------|")
print("")