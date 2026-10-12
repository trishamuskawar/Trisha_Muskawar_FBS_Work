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


class ActionMovie(Movie):
    def __init__(self, id, name, rating, hero):
        super().__init__(id, name, rating)
        self.hero = hero

    def getHero(self):
        return self.hero

    def setHero(self, newhero):
        self.hero = newhero

    def display(self):
        print(f"Hero = {self.hero}")
        super().display()


class ComedyMovie(Movie):
    def __init__(self, id, name, rating, comedian):
        super().__init__(id, name, rating)
        self.comedian = comedian

    def getComedian(self):
        return self.comedian

    def setComedian(self, newcomedian):
        self.comedian = newcomedian

    def display(self):
        print(f"Comedian = {self.comedian}")
        super().display()


m1 = Movie(101, "3 Idiots", 8.8)
a1 = ActionMovie(102, "War", 9.0, "Hrithik")
c1 = ComedyMovie(103, "Hera Pheri", 9.2, "Akshay")

m1.display()
a1.display()
c1.display()