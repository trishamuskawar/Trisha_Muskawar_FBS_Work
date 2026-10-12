class Book:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def calPrice(self):
        print(f'Total Price : {self.price}')


class SchoolBook(Book):
    def __init__(self, id, name, price, tax):
        super().__init__(id, name, price)
        self.tax = tax

    def calPrice(self):
        print(f'Total Price : {self.price + self.tax}')


class EBook(Book):
    def __init__(self, id, name, price, charges):
        super().__init__(id, name, price)
        self.charges = charges

    def calPrice(self):
        print(f'Total Price : {self.price + self.charges}')


b1 = Book(101, "Python", 550)
s1 = SchoolBook(102, "Mathematics", 500, 50)
e1 = EBook(103, "Java", 600, 30)

b1.calPrice()
s1.calPrice()
e1.calPrice()