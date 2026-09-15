#Write a program to find sum of digits of a number.

def sumofDigit(n):
    sum = 0
    while(n > 0):
        d = n % 10
        print(d)
        n = n // 10
        sum = sum + d
    return sum
n = int(input('Enter the digit: '))
res = sumofDigit(n)
print(res)
