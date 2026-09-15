def armstrong(n):
    temp = n
    count = 0
    total = 0

    while(temp > 0):
        count = count + 1
        temp = temp // 10

    temp = n

    while(temp > 0):
        d = temp % 10
        total = total + (d ** count)
        temp = temp // 10

    if(total == n):
        return True
    else:
        return False


n = int(input("Enter a number: "))

res = armstrong(n)

if(res):
    print("Armstrong number")
else:
    print("Not an Armstrong number")