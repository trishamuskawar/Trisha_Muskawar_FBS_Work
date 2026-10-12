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


class SchoolStudent(Student):
    def __init__(self, roll_no, name, marks, standard):
        super().__init__(roll_no, name, marks)
        self.standard = standard

    def getStandard(self):
        return self.standard

    def setStandard(self, newstandard):
        self.standard = newstandard

    def display(self):
        print(f"Standard = {self.standard}")
        super().display()


class CollegeStudent(Student):
    def __init__(self, roll_no, name, marks, branch):
        super().__init__(roll_no, name, marks)
        self.branch = branch

    def getBranch(self):
        return self.branch

    def setBranch(self, newbranch):
        self.branch = newbranch

    def display(self):
        print(f"Branch = {self.branch}")
        super().display()


s1 = Student(101, "Utpal", 89)
ss1 = SchoolStudent(102, "Rahul", 85, 10)
cs1 = CollegeStudent(103, "Trisha", 92, "CSE")

s1.display()
ss1.display()
cs1.display()