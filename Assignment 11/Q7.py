li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]

li3 = []

for i in li1:
    if i in li2:
        li3.append(i)

print("Intersection : ", li3)



