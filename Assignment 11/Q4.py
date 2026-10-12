#Python Program to Find the Second Largest Number in a List Using Bubble Sort

li = [10, 49, 20, 78, 50, 40]

for i in range(0, 6):
    for j in range(0, 5-i):
        if(li[j] > li[j+1]):
            li[j], li[j+1] = li[j+1], li[j]

print(li)
print("second largest number is: ", li[4])