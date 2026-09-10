# To neglect positional para concept.
# Assign value to parameter in fuction call.
# Name of parametr in function definition and function call should be same.
# Flow from right to left (why - positional para flow from left to right).

def emp(id, name, sal, dep):
    print('ID:', id)
    print('Name:', name)
    print('Salary:', sal)
    print('Department:', dep)

emp(name = 'Trisha', id = 101, dep = 'HR', sal = 25000)