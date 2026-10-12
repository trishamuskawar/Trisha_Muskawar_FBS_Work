# def add():
#     print("This is the add function.")
# add(1)

class Employee:
    def __init__(self):
        print("This is the constructor of the class Employee.")
    def display(self):
        print("This is the display function of the class Employee.")
e1 = Employee()
e2 = Employee()
print(f"id e1 = {id(e1)}")
print(f"id e2 = {id(e2)}")