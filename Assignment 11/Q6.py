li1 = [1, 2, 3]
li2 = [4, 5, 6]
li3 = []

li3.extend(li1)
li3.extend(li2)
li3 = list(set(li3))
print("Union : ", li3)