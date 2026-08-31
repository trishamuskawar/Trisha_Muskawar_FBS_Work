#Convert the time entered in hh,min and sec into seconds.

num1 = int(input("Enter the hours: "))
num2 = int(input("Enter the minutes: "))    
num3 = int(input("Enter the seconds: "))

hours = num1 * 60
minutes = num2 * 60
hours1 = hours * 60
total_seconds = hours1 + num3 + minutes

# print("The hours in seconds is: ", hours)
# print("The minutes in seconds is: ", minutes)
# print("The seconds in seconds is: ", seconds)
print("The total seconds is: ", total_seconds)
