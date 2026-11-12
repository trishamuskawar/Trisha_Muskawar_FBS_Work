class Shirt:
    def __init__(self, sid=0, sname=" ", type=" ", price=0, size=0):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
    
    def ShowShirt(self):
        print(f"Shirt Id = {self.sid}, Name = {self.sname}, Type = {self.type}, Price = {self.price}, Size = {self.size}")

    def __del__(self):
        print(f"Shirt {self.sname} is deleted")

s1 = Shirt(101, "Cotton", "Casual", 550, 40)
s2 = Shirt(102, "Denim", "Formal", 600, 42)
s3 = Shirt()

s1.ShowShirt()
s2.ShowShirt()
s3.ShowShirt()