li = [10, 12, 15, 20, 24, 30, 35]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

for ind in range(0, 7):
    if li[ind] % m == 0 and li[ind] % n == 0:
        print(li[ind], end=" ")