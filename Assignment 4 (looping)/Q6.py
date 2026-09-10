num = int(input("enter number: "))
for i in range(2, num):
    if(num % i == 0):
        print(num, "is not prime number.")
        # break
        continue
else:
    print(num, "is prime number.")
    