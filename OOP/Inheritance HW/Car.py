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


class ElectricCar(Car):
    def __init__(self, no, name, price, battery):
        super().__init__(no, name, price)
        self.battery = battery

    def getBattery(self):
        return self.battery

    def setBattery(self, newbattery):
        self.battery = newbattery

    def display(self):
        print(f"Battery = {self.battery}")
        super().display()


class SportsCar(Car):
    def __init__(self, no, name, price, speed):
        super().__init__(no, name, price)
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def setSpeed(self, newspeed):
        self.speed = newspeed

    def display(self):
        print(f"Speed = {self.speed}")
        super().display()


c1 = Car(101, "BMW", 5000000)
e1 = ElectricCar(102, "Tesla", 6000000, "100 kWh")
s1 = SportsCar(103, "Ferrari", 8000000, 320)

c1.display()
e1.display()
s1.display()