class Movie:
    def __init__(self, id, name, rating):
        self.id = id
        self.name = name
        self.rating = rating

    def calRating(self):
        print(f'Total Rating : {self.rating}')


class ActionMovie(Movie):
    def __init__(self, id, name, rating, bonus):
        super().__init__(id, name, rating)
        self.bonus = bonus

    def calRating(self):
        print(f'Total Rating : {self.rating + self.bonus}')


class ComedyMovie(Movie):
    def __init__(self, id, name, rating, bonus):
        super().__init__(id, name, rating)
        self.bonus = bonus

    def calRating(self):
        print(f'Total Rating : {self.rating + self.bonus}')


m1 = Movie(101, "3 Idiots", 8.0)
a1 = ActionMovie(102, "War", 8.0, 1.0)
c1 = ComedyMovie(103, "Hera Pheri", 8.0, 0.5)

m1.calRating()
a1.calRating()
c1.calRating()