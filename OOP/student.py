class Student:
    # inName = "FBS"
    # @staticmethod
    stCount = 0
    def setInName(niname):
        Student.inName = niname

    def __init__(self, frn, name, bname):
        self.frn = frn
        self.name = name
        self.bname = bname
        Student.stCount += 1
    #     self.iname = iname

    # def getFRN(self):
    #     return self.frn
    # def setFRN(self, newfrn):
    #     self.frn = newfrn

    # def getName(self):
    #     return self.name
    # def setName(self, newname):
    #     self.name = newname

    # def getBatchName(self):
    #     return self.bname
    # def setBatchName(self, newbname):
    #     self.bname = newbname

    # def getInstituteName(self):
    #     return self.iname
    # def setInstituteName(self, newiname):
    #     self.iname = newiname

    # def display(self):
    #     print(f"FRN = {self.frn}, Name = {self.name}, Batch Name = {self.bname}, Institute Name = {self.iname}")

    def display(self):
            print(f"FRN = {self.frn}\t Name = {self.name}\t Batch Name = {self.bname}\t Student Count = {Student.stCount}")
#Employee ends here

class PlacedStudent(Student):
     def __init__(self, frn, name, bname, cName):
        super().__init__(frn, name, bname)
        self.cName = cName
     def setcName(self, cName):
        self.cName = cName
     def getcName(self):
        return self.cName 
     def display(self):
        print(f"CName = {self.cName}")
        super().display()

s1 = Student("65", "Neha", "July/Aug")
s2 = Student("66", "Utpal", "July/Aug")
s3 = Student("67", "Sushma", "July/Aug")
s4 = PlacedStudent("68", "Trisha", "July/Aug", "Google")
s5 = PlacedStudent("69", "Rohit", "July/Aug", "Microsoft")
print(Student.stCount)

# s1 = Student("65", "Trisha", "July/Aug", "FBS")
# s2 = Student("66", "Utpal", "July/Aug", "FBS")
# print(s1.getName())
# s1.display()
# s2.display()
# s2.setName("Sushma")
# s2.display()
# print(Student.inName)
# Student.setInName("Firstbit Solutions")
# print(Student.inName)