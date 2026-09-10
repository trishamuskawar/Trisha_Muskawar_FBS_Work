#1. To pass multiple parameters with meaning
#2. Mention double asterisk(**) symbol before parameter name in function definition.
#3. Passed data will be stored in dictionary format.
#4. Use for loop to iterate values on dict.items() and print them.

# def emp(**data):
#     for key, value in data.items():
#         print(type(data))

# emp(id=101, name='Trisha', sal=40000, dep='IT')

def emp(**data):
    for key, value in data.items():
        print(key, ':', value)

emp(id=101, name='Trisha', sal=40000, dep='IT')