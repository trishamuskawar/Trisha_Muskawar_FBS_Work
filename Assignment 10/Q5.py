li = [10, 20, 30, 40, 30, 50]

num = int(input("Enter the element: "))
count = 0

for ind in range(0, 6):
    if(li[ind] == num):
        count += 1
print(f"{num} is present in list.")
print(f"{num} is present {count} times.")