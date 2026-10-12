li = [10, 20, 30, 20, 40, 10, 50]

new_li = [0, 0, 0, 0, 0, 0, 0]
count = 0

for ind in range(0, 7):

    duplicate = False

    for j in range(0, count):
        if(li[ind] == new_li[j]):
            duplicate = True

    if(duplicate == False):
        new_li[count] = li[ind]
        count += 1

print("Unique elements:")

for ind in range(0, count):
    print(new_li[ind], end=" ")