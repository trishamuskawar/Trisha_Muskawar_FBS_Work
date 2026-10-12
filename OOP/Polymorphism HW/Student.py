class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calMarks(self):
        print(f'Total Marks : {self.marks}')


class SchoolStudent(Student):
    def __init__(self, roll_no, name, marks, activity_marks):
        super().__init__(roll_no, name, marks)
        self.activity_marks = activity_marks

    def calMarks(self):
        print(f'Total Marks : {self.marks + self.activity_marks}')


class CollegeStudent(Student):
    def __init__(self, roll_no, name, marks, practical_marks):
        super().__init__(roll_no, name, marks)
        self.practical_marks = practical_marks

    def calMarks(self):
        print(f'Total Marks : {self.marks + self.practical_marks}')


s1 = Student(101, "Utpal", 70)
ss1 = SchoolStudent(102, "Rahul", 70, 10)
cs1 = CollegeStudent(103, "Trisha", 70, 25)

s1.calMarks()
ss1.calMarks()
cs1.calMarks()