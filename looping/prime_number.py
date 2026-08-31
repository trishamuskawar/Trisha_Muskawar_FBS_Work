# num = int(input('Enter a number to check if it is prime: '))

# for i in range(2, num):
#     if(num % i == 0):
#         print(f"{num} is not a prime number")
#         break
# else:
#     print(f"{num} is a prime number")


# n = int(input('Enter a number to check if it is prime: '))

# for i in range(2, n):
#     if(n % i == 0):
#         print(f"{n} is not a prime number")
#         break
# else:
#     print(f"{n} is a prime number")

# write a program to print prime number between 1 to 100
n = int(input('Enter value of n= '))

for n in range(2, n+1):
    for i in range(2, n):
        if(n % i ==0):
            break
    else:
        print(n, end='  ')

# write a program to print first n prime numbers.
# n = int(input('Enter the number of prime numbers to print: '))
# count = 0   
# num = 2


# while count < n:
#     for i in range(2, num):
#         if(num % i == 0):
#             break
#     else:
#         print(num, end='  ')
#         count += 1
#     num += 1
