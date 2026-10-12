r = 20
l = 50
b = 40
cost = 35

semi_circle = 3.14 * r

rectangle = 2 * (l + b)

perimeter = semi_circle + rectangle

total_wire = perimeter * 5

total_cost = total_wire * cost

print("Total wire required:", total_wire, "m")
print("Total cost of fencing: Rs.", total_cost)