class Car:
    def __init__(self, no, name, price):
        self.no = no
        self.name = name
        self.price = price

    def calPrice(self):
        print(f'Total Price : {self.price}')


class ElectricCar(Car):
    def __init__(self, no, name, price, battery_cost):
        super().__init__(no, name, price)
        self.battery_cost = battery_cost

    def calPrice(self):
        print(f'Total Price : {self.price + self.battery_cost}')


class SportsCar(Car):
    def __init__(self, no, name, price, performance_cost):
        super().__init__(no, name, price)
        self.performance_cost = performance_cost

    def calPrice(self):
        print(f'Total Price : {self.price + self.performance_cost}')


c1 = Car(101, "BMW", 5000000)
e1 = ElectricCar(102, "Tesla", 6000000, 200000)
s1 = SportsCar(103, "Ferrari", 8000000, 300000)

c1.calPrice()
e1.calPrice()
s1.calPrice()