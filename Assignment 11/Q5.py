li = ["cat", "elephant", "dog", "hi"]

for i in range(0, 4):
    for j in range(0, 3 - i):

        count1 = 0
        for ch in li[j]:
            count1 = count1 + 1

        count2 = 0
        for ch in li[j + 1]:
            count2 = count2 + 1

        if count1 > count2:
            li[j], li[j + 1] = li[j + 1], li[j]

print(li)