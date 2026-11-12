class Emp:
    def __init__(self, id,name,sal):
        self.__id = id
        self.__name=name
        self.__sal=sal
    def getId(self):
        return self.__id
    def setId(self,nid):
        self.__id=nid
    def __str__(self):
        return f"ID={self.__id} Name={self.__name} Sal={self.__sal}"
class Hr(Emp):
    def __str__(self):
        print(self.__id)
        return super().__str__()
e1 = Emp(1,"Trisha", 50000)
print(e1.getId())
e1.setId(3)
print(e1.getId())
h1 = Hr(12,"Utpal", 60000)
print(h1.getId())