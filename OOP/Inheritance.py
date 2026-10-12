# class Employee:
#     def __init__(self, id1, name1, sal1):
#         self.id = id1
#         self.name = name1
#         self.salary = sal1

#     def getId(self):
#         return self.id
#     def setId(self, newid):
#         self.id = newid

#     def getName(self):
#         return self.name                
#     def setName(self, newname):
#         self.name = newname

#     def getSalary(self):
#         return self.salary      
#     def setSalary(self, newsal):
#         self.salary = newsal

#     def display(self):
#         print(f"ID = {self.id}, Name = {self.name}, Salary = {self.salary}")

# class Hr(Employee):
#     def __init__(self, id, name, sal, com):
#         super().__init__(id, name, sal)
#         self.com = com
#     def getCom(self):
#         return self.com
#     def setCom(self, ncom):
#         self.com = ncom
#     def display(self):
#         print(f"Com = {self.com}")
#         super().display()

# class Devloper(Employee):
#     def __init__(self, id, name, sal, bonus):
#         super().__init__(id, name, sal)
#         self.bonus = bonus
#     def getBonus(self):
#         return self.bonus
#     def setBonus(self, ncom):
#         self.bonus = ncom
#     def display(self):
#         print(f"Bonus = {self.bonus}")
#         return super().display()

# e1 = Employee(1, "Rahul", 3333)
# h1 = Hr(7, "Trisha", 8438, 1500)
# d1 = Devloper(8, "John", 5000, 563)
# e1.display()
# h1.display()
# d1.display()

class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name
    def setName(self, newname):
        self.name = newname

    def getSal(self):
        return self.sal
    def setSal(self, newid):
        self.sal = newid

    def calSal(self):
        print(f'Total salary : {self.sal}')

    def display(self):
        print(f"Id = {self.id}\t Name = {self.name}\t Sal = {self.sal}")

class Hr(Employee):
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com
    def getCom(self):
        return self.com
    def setCom(self, ncom):
        self.com = ncom

    def calSal(self):
        print(f'Total salary : {self.sal + self.com}')

    def display(self):
        print(f'Com = {self.com}\t')
        return super().display()

class Developer(Employee):
    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus
    def getBonus(self):
        return self.bonus
    def setBonus(self, ncom):
        self.bonus = ncom

    def calSal(self):
        print(f'Total salary : {self.sal + self.bonus}')

    def display(self):
        print(f'Bonus = {self.bonus}\t')
        return super().display()

e1 = Employee(1, 'Trisha', 200000)
h1 = Hr(2, 'Utpal', 150000, 2000)
d1 = Developer(3, 'Shivansh', 200000, 3000)
e1.calSal()
h1.calSal()
d1.calSal()