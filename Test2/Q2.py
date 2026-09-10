first_digit = int(input("Enter a first digit: "))
second_digit = int(input("Enter a second digit: "))
third_digit = int(input("Enter a third digit: "))

if (first_digit == second_digit * 2) and (first_digit == third_digit / 2):
    print("Yes, you have done it")
else:
    print("Please try next time")

