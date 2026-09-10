# to pass multiple para to function.
# Mention asterisk(*) symbol before parameter name in function definition.
# Values will be store in tuple.
# Use for loop to iterate values from tuple and print them.

def addtion(*num):
    sum = 0
    for val in num:
        sum += val
    return sum

res = addtion(10, 20, 30, 40, 50)
print('Addition:', res)