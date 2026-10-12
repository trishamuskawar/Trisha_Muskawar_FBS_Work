li = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to remove: "))

new_li = [0, 0, 0, 0, 0, 0, 0]
count = 0

for ind in range(0, 7):

    if li[ind] != num:
        new_li[count] = li[ind]
        count += 1

print("List after removing:", end=" ")

for ind in range(0, count):
    print(new_li[ind], end=" ")