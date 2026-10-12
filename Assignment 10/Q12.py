li = [2, 3, 4, 5]

square_li = [0, 0, 0, 0]
cube_li = [0, 0, 0, 0]

for ind in range(0, 4):
    square_li[ind] = li[ind] ** 2
    cube_li[ind] = li[ind] ** 3

print("Numbers:", li)
print("Squares:", square_li)
print("Cubes:", cube_li)