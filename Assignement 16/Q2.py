
class Product:
    discount = 10  # Static member: 10% discount

    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def applyDiscount(self):
        discount_amount = self.price * Product.discount / 100
        self.price = self.price - discount_amount

    def ShowProduct(self):
        print(f"Product Id = {self.pid}, Name = {self.pname}, "
              f"Price = {self.price}, Quantity = {self.quantity}")

    def __del__(self):
        print(f"Product {self.pname} is deleted")


p1 = Product(101, "Mobile", 550, 10)
p2 = Product(102, "Laptop", 600, 5)
p3 = Product()

p1.applyDiscount()
p2.applyDiscount()

p1.ShowProduct()
p2.ShowProduct()
p3.ShowProduct()
