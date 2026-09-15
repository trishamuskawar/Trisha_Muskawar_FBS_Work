n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):

    print("Enter marks for student", i)

    m1 = int(input("Enter subject 1 marks: "))
    m2 = int(input("Enter subject 2 marks: "))
    m3 = int(input("Enter subject 3 marks: "))
    m4 = int(input("Enter subject 4 marks: "))
    m5 = int(input("Enter subject 5 marks: "))

    total = m1 + m2 + m3 + m4 + m5

    percentage = total / 5

    print("Percentage of student", i, "=", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average percentage =", average)