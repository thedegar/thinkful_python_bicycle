# Tyler Hedegard 5/11/2016
# Thinkful.com Python Introduction Lesson 3.4
# Bicycle Assignment

from bicycle import Bicycle, BicycleShop, Customer, Wheel, Frame

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
    spokeWheel = Wheel("Spokes",35,40)
    magWheel = Wheel("Mags",25,45)
    fiberWheel = Wheel("Carbon",10,100)
    aluminumFrame = Frame("Aluminum",100,100)
    carbonFrame = Frame("Carbon",50,500)
    steelFrame = Frame("Steel",200,75)
    bmx = Bicycle("BMX",magWheel,steelFrame)
    tenSpeed = Bicycle("10 Speed",spokeWheel,carbonFrame)
    rally = Bicycle("Rally Bike",fiberWheel,carbonFrame)
    mountain = Bicycle("Ridge Rider",spokeWheel,aluminumFrame)
    trike = Bicycle("Trike",spokeWheel,steelFrame)
    moped = Bicycle("MoPed",spokeWheel,steelFrame)
    
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
    
    #Print the current inventory and profit so far
    inventory(ricks)
    print("{} has made ${} profit.".format(ricks.name,int(ricks.profit)))