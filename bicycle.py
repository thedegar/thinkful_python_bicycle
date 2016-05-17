# Tyler Hedegard 5/11/2016
# Thinkful.com Python Introduction Lesson 3.4
# Bicycle Assignment

class Bicycle(object):
    def __init__(self,name,weight,cost):
        self.name = name
        self.weight = weight
        self.cost = cost
        
class BicycleShop(object):
    def __init__(self,name,margin):
        self.name = name
        self.margin = margin
        self.profit = 0
        self.inventory = []
        
    def addInventory(self,Bicycle):
        """Adds a Bicycle to the store's inventory"""
        self.inventory.append(Bicycle)

class Customer(object):
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget
        self.bicycle = []
        
    def buy(self,Bicycle):
        """Adds a Bicycle to the Customer's ownership"""
        self.bicycle.append(Bicycle)
        print("{} now own {}.".format(self.name,self.bicycle))
        
if __name__ == "__main__":
    ricks = BicycleShop("Rick's Bike Shop",0.2)
    bmx = Bicycle("BMX",100,150)
    tenSpeed = Bicycle("10 Speed",100,250)
    rally = Bicycle("Rally Bike",110,800)
    mountain = Bicycle("Ridge Rider",130,350)
    trike = Bicycle("Trike",75,100)
    moped = Bicycle("MoPed",200,350)
    chris = Customer("Chris",200)
    peter = Customer("Peter",500)
    lila = Customer("Lila",1000)
    
    for i in range(3):
        ricks.addInventory(bmx)
        ricks.addInventory(tenSpeed)
        ricks.addInventory(rally)
        ricks.addInventory(mountain)
        ricks.addInventory(trike)
        ricks.addInventory(moped)
    
    print(len(ricks.inventory))
    print(ricks.margin)
    print(ricks.inventory[0].name)