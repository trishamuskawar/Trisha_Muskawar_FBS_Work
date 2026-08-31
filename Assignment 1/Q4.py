#Write a program to enter P, T, R and calculate simple Interest.

num1 = int(input("Enter the Principal amount: "))
num2 = int(input("Enter the Rate of interest: "))
num3 = int(input("Enter the Time period: "))

simple_interest = (num1 * num2 * num3) /100

print("The simple interest is: ", simple_interest)

