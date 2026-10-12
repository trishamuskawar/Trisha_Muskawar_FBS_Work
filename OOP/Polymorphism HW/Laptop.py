class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    def calPrice(self):
        print(f'Total Price : {self.price}')


class GamingLaptop(Laptop):
    def __init__(self, brand, ram, processor, price, graphics_cost):
        super().__init__(brand, ram, processor, price)
        self.graphics_cost = graphics_cost

    def calPrice(self):
        print(f'Total Price : {self.price + self.graphics_cost}')


class BusinessLaptop(Laptop):
    def __init__(self, brand, ram, processor, price, feature_cost):
        super().__init__(brand, ram, processor, price)
        self.feature_cost = feature_cost

    def calPrice(self):
        print(f'Total Price : {self.price + self.feature_cost}')


l1 = Laptop("Lenovo", "8GB", "i5", 50000)
g1 = GamingLaptop("Asus", "16GB", "i7", 80000, 20000)
b1 = BusinessLaptop("HP", "16GB", "i7", 70000, 10000)

l1.calPrice()
g1.calPrice()
b1.calPrice()