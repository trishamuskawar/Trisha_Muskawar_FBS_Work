class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def getRollNo(self):
        return self.roll_no

    def setRollNo(self, newroll_no):
        self.roll_no = newroll_no

    def getName(self):
        return self.name

    def setName(self, newname):
        self.name = newname

    def getMarks(self):
        return self.marks

    def setMarks(self, newmarks):
        self.marks = newmarks

    def display(self):
        print(f"Roll No = {self.roll_no}, Name = {self.name}, Marks = {self.marks}")


s1 = Student(101, "Utpal", 89)
s2 = Student(102, "Trisha", 92)

s1.display()
s2.display()