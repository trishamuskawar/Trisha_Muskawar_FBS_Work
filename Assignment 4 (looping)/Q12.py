num = int(input("Enter a number: "))

temp = num
count = 0
while(temp>0):
    count += 1
    temp = temp//10

temp = num
sum = 0
while (temp > 0):
    d = temp % 10
    temp = temp // 10
    sum = sum + (d ** count)
if (sum == num):
    print(f"{num} is a amstrong number")
else:
    print(f"{num} is not a amstrong number")