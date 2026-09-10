#Write a program to check if given 3 digit number is a palindrome or not using branching.

num = int(input("Enter 3 digit number: "))

temp = num
rev_num = 0

while (temp != 0):
    digit = temp % 10
    rev_num = rev_num * 10 + digit
    temp = temp // 10

if (num == rev_num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
