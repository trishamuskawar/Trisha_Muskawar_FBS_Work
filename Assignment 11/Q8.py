num = 1

for row in range(10):
    li = []

    for col in range(10):
        li.append(num)
        num += 1

    if row % 2 == 1:
        li.reverse()

    print(li)