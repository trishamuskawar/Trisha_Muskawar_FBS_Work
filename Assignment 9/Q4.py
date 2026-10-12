def sumOfSeries(n):
    if(n <= 0):
        return 0
    else:
        return n + sumOfSeries(n - 1)

n = int(input('Enter number : '))
res = sumOfSeries(n)
print(res)