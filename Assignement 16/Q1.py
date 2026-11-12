class Book:
    count = 0

    def __init__(self, bid=0, bname=" ", price=0, author=" "):
        self.bid = bid
        self.bname = bname
        self.price = price
        Book.count += 1
        self.author = author

    @staticmethod
    def getCount():
        return Book.count
    
    def ShowBook(self):
        print(f"Book Id = {self.bid}, Name = {self.bname}, Price = {self.price}, Author = {self.author} ")

    def __del__(self):
        print(f"Book {self.bname} is deleted")

b1 = Book(101, "Python", 550, "John")
b2 = Book(102, "Java", 600, "Smith")
b3= Book( )

b1.ShowBook()
b2.ShowBook()
b3.ShowBook()

print("Total objects created =", Book.getCount())
