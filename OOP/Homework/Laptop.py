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


l1 = Laptop("Lenovo", "8GB", "i5")
l2 = Laptop("HP", "16GB", "i7")

l1.display()
l2.display()