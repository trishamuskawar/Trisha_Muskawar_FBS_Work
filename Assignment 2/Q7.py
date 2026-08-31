#Find the sum of three-digit number.

n = int(input('Enter the three digit number: '))

d1 = n % 10
n1 = n // 10
print(d1)

d2 = n1 % 10
n2 = n1 // 10
print(d2)

d3 = n2 % 10
n3 = n2 // 10
print(d3)

total = d1 + d2 + d3
print(f'The sum of the digits of {n} is {total}') 