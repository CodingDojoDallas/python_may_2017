#create a class bike
class Bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self,x):
        self.miles += 10
        print ("Riding " * x), self.miles
        return self
    def reverse(self,x):
        self.miles -= 5
        print ("Reversing " * x), self.miles
        return self


bike1 = Bike(100,25,10)
bike2 = Bike(200,20,10)
bike3 = Bike(150,15,20)

bike1.ride(3).reverse(1).displayInfo()
bike2.ride(2).reverse(2).displayInfo()
bike3.reverse(3).displayInfo()






