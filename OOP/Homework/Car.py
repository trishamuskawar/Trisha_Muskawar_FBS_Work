class Car:
    def __init__(self, no, name, price):
        self.no = no
        self.name = name
        self.price = price

    def getNo(self):
        return self.no

    def setNo(self, newno):
        self.no = newno

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price

    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Car No = {self.no}, Name = {self.name}, Price = {self.price}")


c1 = Car(101, "BMW", 5000000)
c2 = Car(102, "Audi", 6000000)

c1.display()
c2.display()