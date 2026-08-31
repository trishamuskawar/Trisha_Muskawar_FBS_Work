# write a program to print table of a number entered by the user using while loop
num = int(input("Enter a number to print its table: "))
i = 1
while (i <= 10):
    print(f"{num} * {i} = {num * i}")
    i += 1