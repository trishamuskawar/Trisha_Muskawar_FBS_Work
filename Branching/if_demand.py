#IF syntax:
#if condition:
    #block of code to be executed if the condition is true
    #b2
    #b3
    #b4
#line after if block of code will be executed regardless of the condition

num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("The number is even.")
print("the number is odd.")