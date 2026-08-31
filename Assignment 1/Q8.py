#Write a program to convert days into years, weeks and days.

num1 = int(input("Enter the number of days: "))

years = num1 / 365
weeks = (num1 % 365) / 7
days = (num1 % 365) % 7

print("The number of years is: ", int(years))
print("The number of weeks is: ", int(weeks))
print("The number of days is: ", int(days))