#Convert distant given in feet and inches into meter and centimeter.

n1 = int(input('Enter the distance in feet:'))
n2 = int(input('Enter the distance in inches:'))

meter = n1 *0.3048
centimeter = n1 * 30.48

centimeter1 = n2 * 2.54
meter1 = n2 * 0.0254

print(f'{n1} feet in meter is {meter} and in centimeter is {centimeter}')
print(f'{n2} inches in meter is {meter1} and in centimeter is {centimeter1}')