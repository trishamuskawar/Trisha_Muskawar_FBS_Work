li = [10, 21, 30, 45, 50, 63]

new_li = [0, 0, 0, 0, 0, 0]
count = 0

for ind in range(0, 6):

    if li[ind] % 2 != 0:
        new_li[count] = li[ind]
        count += 1

print("List after removing even numbers:", end=" ")

for ind in range(0, count):
    print(new_li[ind], end=" ")