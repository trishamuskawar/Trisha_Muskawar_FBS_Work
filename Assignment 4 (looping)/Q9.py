#9. WAP to print all numbers in a range divisible by a given number.

n = int(input('Enter the ending number: '))
divisior = int(input('Enter the divisor: '))
for i in range(1,n+1):
    if (i % divisior == 0):
        print(f'{i} is divisible by {divisior}')
    else:
        print(f"{i} is not divisible by {divisior}")
