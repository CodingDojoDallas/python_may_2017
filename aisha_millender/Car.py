#create a class Car

class Car(object):
    def __init__(self,price,speed,fuel,mileage,tax=0):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax

    def __str__(self):
        string_format = "Price: {} Speed: {} Fuel: {} Mileage: {} Tax: {}"
        return string_format.format(
            self.price,
            self.speed,
            self.fuel,
            self.mileage,
            self.tax
        )

    def display_all(self):
        tax = 0
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        print "Price: ",self.price
        print "Speed: ",self.speed
        print "Fuel: ",self.fuel
        print "Mileage: ",self.mileage
        print "Tax: ",self.tax


car1 = Car(2000,"35mph","Full","15mpg")
car2 = Car(2000,"5mph","Not Full","15mpg")
car3 = Car(2000,"15mph","Kind of Full","15mpg")
car4 = Car(2000,"25mph","Full","15mpg")
car5 = Car(2000,"45mph","Empty","15mpg")
car6 = Car(20000000,"35mph","Empty","15mpg")

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
