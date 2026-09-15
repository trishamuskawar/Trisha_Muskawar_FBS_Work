#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n

def sumofSeries(n):
    if(n <= 0):
        return 0
    else:
        return n + sumofSeries(n-1)
n = int(input('Enter the number: '))
res = sumofSeries(n)
print(res)



#b. 1!+ 2! + 3! + 4!+..... + n!
def sumofSeries(n):
    sum = 0

    for j in range(1, n+1):
        fact = 1

        for i in range(1, j+1):
            fact = fact * i
        sum = sum + fact

    return sum

n = int(input("Enter a number: "))
res = sumofSeries(n)
print(res)


#c. 1^1 + 2^2 + 3^3+ ...... n^n
def sumofSeries(n):
    sum = 0

    for i in range(1, n+1):
        sum = sum + (i ** i)
    return sum

n = int(input("Enter a number: "))
res = sumofSeries(n)
print(res)
