length = int(input('Enter the length: '))
breadth = int(input('Enter the breadth: '))
radius = int(input('enter the radius: '))

area_rectangle = length * breadth
area_semicircle = 1/2 * 3.14 * radius**2
total_area = area_rectangle + area_semicircle

perimeter_rectangle = (length *2) + breadth
perimeter_semicircle = 3.14 * radius
total_perimeter = perimeter_rectangle + perimeter_semicircle

print(f'{total_area} is the area of figure.')
print(f'{total_perimeter} is the perimeter of figure.')