class Movie:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def getId(self):
        return self.id

    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getRating(self):
        return self.rating

    def setRating(self, newrating):
        self.rating = newrating

    def display(self):
        print(f"Movie Id = {self.id}, Name = {self.name}, Rating = {self.rating}")


m1 = Movie(101, "3 Idiots", 8.8)
m2 = Movie(102, "Fidaa", 9.9)

m1.display()
m2.display()