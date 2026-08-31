#Write a program to calculate the percentage of student based on marks of any 5 subjects.

num1 = int(input("Enter marks of subject 1: "))
num2 = int(input("Enter marks of subject 2: ")) 
num3 = int(input("Enter marks of subject 3: "))
num4 = int(input("Enter marks of subject 4: ")) 
num5 = int(input("Enter marks of subject 5: "))

total = num1 + num2 + num3 + num4 + num5
percentage = (total / 500) * 100

print("Total marks:", total)
print("Percentage:", percentage)
