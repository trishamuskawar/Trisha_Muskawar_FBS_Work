li = [1, 2, 3, 4, 5]
newli = [x**2 for x in li]
print(newli)

newli2 = [x+10 for x in li]
print(newli2)

#WAC to print square of odd number from the list
 
li1 = [3, 9, 10, 20, 11, 7, 2, 5]
newli3 = [ x**2 for x in li1 if x%2!=0]
print(newli3)

li2 = [3, 9, 10, 22, 11, 7, 2, 5]
newli4 = [x*x for x in li2 if x%2!=0]
print(newli4)

li3 = [3, 9, 10, 22, 11, 7, 2, 5]
