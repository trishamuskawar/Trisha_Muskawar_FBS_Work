gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))

if (gender == "F"):
    if (age > 18):
        print("girls are eligible for marriage")
    else:
        print("girls are not eligible for marriage")
else:
    if (age > 21):
        print("Boys are eligible for marriage")
    else:
        print("Boys are not eligible for marriage")

        