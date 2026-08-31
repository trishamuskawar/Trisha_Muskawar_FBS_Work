gender = input('Enter gender(M/F): ')
age = int(input('Enter age:'))

if (gender == 'F'):
    if (age >=18):
        print('She is eligible for marriage.')
    else:
        print('She is not eligible for marriage.')
else:
    if (age >=21):
        print('He is eligible for marriage.')
    else:
        print('He is not eligible for marriage')