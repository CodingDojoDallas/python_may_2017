# create a class with attributes price,item name, weight, brand, cost, status: default "for sale"

class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price += float(tax)
        return self

    def returns(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        else:
            self.status = "for sale"
        return self


    def __str__(self):
        string_format = "Price: {} Item_Name: {} Weight: {} Brand: {} Cost: {} Status: {}"
        return string_format.format(
            self.price,
            self.item_name,
            self.weight,
            self.brand,
            self.cost,
            self.status
        )

    def info(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.cost
        print self.status
        return self


product1 = Product(200,"jeans","15lbs","Paige Denim",150)
product2 = Product(120,"dress", "15lbs","Zulily",50)
product1.returns("defective").info()
product2.sell().addTax(0.15).info()