num1 = int(input("Enter marks of Principal Amount: "))
num2 = int(input("Enter the Rate of interest: "))

compound_interest = num1 * (1 + num2 / 100) ** 1 - num1

print("The compound interest is: ", compound_interest)
