#Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input('Enter number a:'))
b = int(input('Enter number b:'))
c = int(input('Enter number c:'))

sum = a + b + c

if (sum == 180):
    print('The triangle is valid')
else:
    print('The triangle is not valid')
