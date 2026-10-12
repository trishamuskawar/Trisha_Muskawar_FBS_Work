class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Roll No = {self.roll_no}, Name = {self.name}, Marks = {self.marks}")
s1 = Student(101, "Utpal", 89)
s2 = Student(102, "Trisha", 92)
s1.display()
s2.display()