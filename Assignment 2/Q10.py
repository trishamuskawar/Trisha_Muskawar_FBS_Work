#Write a program to reverse three-digit number.

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

print(f'The reverse of the three digit number {n} is {d1}{d2}{d3}')