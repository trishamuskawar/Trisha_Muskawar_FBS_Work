#Write a Program to input two angles from user and find third angle of the triangle.

num1 = int(input("Enter the first angle: "))
num2 = int(input("Enter the second angle:"))

num3 = 180 - (num1 + num2)

print("The Third angle of the triangle is: ", num3)
