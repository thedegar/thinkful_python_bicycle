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
        self.profit += Bicycle.cost*self.margin

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
        
