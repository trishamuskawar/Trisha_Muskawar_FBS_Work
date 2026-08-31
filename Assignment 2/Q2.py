#Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

num = int(input('Enter temperature in celcius: '))

F = (num * 1.8) + 32
print(f'{num} temperature in celcius is {F} in fahrenheit')