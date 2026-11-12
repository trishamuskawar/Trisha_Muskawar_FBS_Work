
class Shirt:
    increment = 10  # Static variable: 10% increment

    def __init__(self, sid=0, sname="", type="", price=0, size="Small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def calculatePrice(self):
        if self.size.lower() == "small":
            self.price = self.price
        elif self.size.lower() == "medium":
            self.price = self.price + (self.price * Shirt.increment / 100)
        elif self.size.lower() == "large":
            self.price = self.price + (self.price * Shirt.increment / 100 * 2)
        elif self.size.lower() == "xlarge":
            self.price = self.price + (self.price * Shirt.increment / 100 * 3)

    def ShowShirt(self):
        print(f"Shirt Id = {self.sid}, Name = {self.sname}, "
              f"Type = {self.type}, Price = {self.price}, Size = {self.size}")

    def __del__(self):
        print(f"Shirt {self.sname} is deleted")


s1 = Shirt(101, "Cotton", "Casual", 1000, "Small")
s2 = Shirt(102, "Denim", "Formal", 1000, "Medium")
s3 = Shirt(103, "Linen", "Casual", 1000, "Large")
s4 = Shirt(104, "Silk", "Formal", 1000, "Xlarge")
s5 = Shirt()

s1.calculatePrice()
s2.calculatePrice()
s3.calculatePrice()
s4.calculatePrice()

s1.ShowShirt()
s2.ShowShirt()
s3.ShowShirt()
s4.ShowShirt()
s5.ShowShirt()
