class Book:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getPrice(self):
        return self.price

    def setPrice(self, newprice):
        self.price = newprice

    def display(self):
        print(f"Book Id = {self.id}, Name = {self.name}, Price = {self.price}")


class SchoolBook(Book):
    def __init__(self, id, name, price, standard):
        super().__init__(id, name, price)
        self.standard = standard

    def getStandard(self):
        return self.standard

    def setStandard(self, newstandard):
        self.standard = newstandard

    def display(self):
        print(f"Standard = {self.standard}")
        super().display()


class EBook(Book):
    def __init__(self, id, name, price, size):
        super().__init__(id, name, price)
        self.size = size

    def getSize(self):
        return self.size

    def setSize(self, newsize):
        self.size = newsize

    def display(self):
        print(f"Size = {self.size}")
        super().display()


b1 = Book(101, "Python", 550)
s1 = SchoolBook(102, "Mathematics", 500, 10)
e1 = EBook(103, "Java", 600, "5 MB")

b1.display()
s1.display()
e1.display()