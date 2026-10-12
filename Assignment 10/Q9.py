li = [39, 48, 59, 20, 68, 99]

even_li = [0, 0, 0]
odd_li = [0, 0, 0]

even_count = 0
odd_count = 0

for ind in range(0,6):
    if(li[ind] % 2 == 0):
        even_li[even_count] = li[ind]
        even_count += 1
    else:
        odd_li[odd_count] = li[ind]
        odd_count +=1
print("Even element: ", even_li)
print("Odd element: ", odd_li)