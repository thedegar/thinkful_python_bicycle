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
        
    def sell(self,Bicycle):
        self.inventory.remove(Bicycle)

class Customer(object):
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget
        self.bicycle = []
        
    def buy(self,bike,shop):
        """Adds a Bicycle to the Customer's ownership"""
        if bike in shop.inventory:
            cost = bike.cost*(1+shop.margin)
            self.bicycle.append(bike)
            self.budget -= cost
            shop.sell(bike)
        print("{}, you now own a {}.".format(self.name,bike.name))
        print("You bought it for ${} and have ${} left.".format(cost,self.budget))
        
def options(customer,shop):
    """Prints out the customer name and the bikes he can afford"""
    print(customer.name + ", you can buy:")
    bikes = []
    for i in shop.inventory:
        if i.name not in bikes and i.cost * (1+shop.margin) <= customer.budget:
            bikes.append(i.name)
            print("    " + i.name + " for $" + str(i.cost*(1+shop.margin)))

def inventory(shop):
    """Print out the inventory for a bike shop"""
    bikes = {}
    for i in shop.inventory:
        if i.name not in bikes:
            bikes[i.name] = 1
        else:
            bikes[i.name] += 1
    print(shop.name + " has the following inventory:")
    print(bikes)
        

if __name__ == "__main__":
    #Create a bike shop with 6 bike models
    ricks = BicycleShop("Rick's Bike Shop",0.2)
    bmx = Bicycle("BMX",100,150)
    tenSpeed = Bicycle("10 Speed",100,250)
    rally = Bicycle("Rally Bike",110,800)
    mountain = Bicycle("Ridge Rider",130,350)
    trike = Bicycle("Trike",75,100)
    moped = Bicycle("MoPed",200,350)
    
    for i in range(3):
        ricks.addInventory(bmx)
        ricks.addInventory(tenSpeed)
        ricks.addInventory(rally)
        ricks.addInventory(mountain)
        ricks.addInventory(trike)
        ricks.addInventory(moped)
    
    #Create 3 customers
    chris = Customer("Chris",200)
    peter = Customer("Peter",500)
    lila = Customer("Lila",1000)
    
    #Print each customer and the bikes they can buy
    options(chris,ricks)
    options(peter,ricks)
    options(lila,ricks)
    
    #Print current inventory for a shop
    inventory(ricks)
    
    #Buy one bike per customer
    chris.buy(bmx,ricks)
    peter.buy(moped,ricks)
    lila.buy(rally,ricks)
    inventory(ricks)