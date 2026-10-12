li = [[1, 5], [2, 3], [4, 1], [6, 4]]

for i in range(0, 4):
    for j in range(i + 1, 4):
        if li[i][1] > li[j][1]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp

print(li)
