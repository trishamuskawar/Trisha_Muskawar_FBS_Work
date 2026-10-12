class Employee:
    def __init__(self, id1, name1, sal1):
        self.id = id1
        self.name = name1
        self.salary = sal1

    def getId(self):
        return self.id
    def setId(self, newid):
        self.id = newid

    def getName(self):
        return self.name                
    def setName(self, newname):
        self.name = newname

    def getSalary(self):
        return self.salary      
    def setSalary(self, newsal):
        self.salary = newsal

    def display(self):
        print(f"ID = {self.id}, Name = {self.name}, Salary = {self.salary}")

e1 = Employee(101, "Utpal", 50000)
e2 = Employee(102, "Trisha", 60000)
print(e1.getName())
e1.display()
e2.display()
e2.setSalary(70000)
e2.display()