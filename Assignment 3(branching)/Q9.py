subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))    
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))
subject5 = int(input("Enter marks for subject 5: "))

total_marks = (subject1 + subject2 + subject3 + subject4 + subject5)/5 
print("The total marks obtained by the student is: ", total_marks)

if(total_marks > 90):
    print("The student has passed with first class.")
elif(total_marks > 80):
    print("The student has passed with second class.")
elif(total_marks > 70):
    print("The student has passed with third class.")
else:
    print("The student has failed.")
