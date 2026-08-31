#Write a program to calculate profit or loss.

cp = int(input("Enter the cost price: " ))
sp = int(input("Enter the selling price: " ))

profit = sp - cp
loss = cp - sp

if (sp > cp):
    print("The transaction is profitable.")
elif (sp < cp): 
    print("The transaction is at a loss.")
else:
    print('even')
