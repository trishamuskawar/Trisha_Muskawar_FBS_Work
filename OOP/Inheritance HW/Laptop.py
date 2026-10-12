class Laptop:
    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def getBrand(self):
        return self.brand

    def setBrand(self, newbrand):
        self.brand = newbrand

    def getRam(self):
        return self.ram

    def setRam(self, newram):
        self.ram = newram

    def getProcessor(self):
        return self.processor

    def setProcessor(self, newprocessor):
        self.processor = newprocessor

    def display(self):
        print(f"Laptop Brand = {self.brand}, RAM = {self.ram}, Processor = {self.processor}")


class GamingLaptop(Laptop):
    def __init__(self, brand, ram, processor, graphics):
        super().__init__(brand, ram, processor)
        self.graphics = graphics

    def getGraphics(self):
        return self.graphics

    def setGraphics(self, newgraphics):
        self.graphics = newgraphics

    def display(self):
        print(f"Graphics = {self.graphics}")
        super().display()


class BusinessLaptop(Laptop):
    def __init__(self, brand, ram, processor, weight):
        super().__init__(brand, ram, processor)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setWeight(self, newweight):
        self.weight = newweight

    def display(self):
        print(f"Weight = {self.weight}")
        super().display()


l1 = Laptop("Lenovo", "8GB", "i5")
g1 = GamingLaptop("Asus", "16GB", "i7", "RTX 4060")
b1 = BusinessLaptop("HP", "16GB", "i7", "1.5 kg")

l1.display()
g1.display()
b1.display()