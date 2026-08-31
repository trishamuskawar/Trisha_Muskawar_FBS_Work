#Program to Find the Roots of a Quadratic Equation
num1 = int(input("Enter the value of a: "))
num2 = int(input("Enter the value of b: "))
num3 = int(input("Enter the value of c: "))

root1 = (-num2 + (num2 ** 2 - 4 * num1 * num3) ** 0.5) / (2 * num1)
root2 = (-num2 - (num2 ** 2 - 4 * num1 * num3) ** 0.5) / (2 * num1)

print("The roots of the quadratic equation are: ", root1, "and", root2)
