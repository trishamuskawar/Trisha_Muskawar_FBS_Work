#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.


ticket = int(input("Enter  person ticket amount: "))

age1 = int(input("Enter 1st person  age: "))
if(age1<12):
    amount1 = ticket - (ticket * 30 / 100)
elif (age1 > 59):
    amount1 = ticket - (ticket * 50 / 100)
else:
    amount1 = ticket

age2 = int(input("Enter 2nd person age:  "))
if(age2<12):
    amount2 = ticket - (ticket * 30 / 100)
elif (age2 > 59):
    amount2 = ticket - (ticket * 50 / 100)
else:
    amount2 = ticket

age3 = int(input("Enter 3rd person age: "))
if(age3<12):
    amount3 = ticket - (ticket * 30 / 100)
elif (age3 > 59):
    amount3 = ticket - (ticket * 50 / 100)
else:
    amount3 = ticket

age4 = int(input("Enter 4th person age: "))
if(age4<12):
    amount4 = ticket - (ticket * 30 / 100)
elif (age4 > 59):
    amount4 = ticket - (ticket * 50 / 100)
else:
    amount4 = ticket

age5 = int(input("Enter 5th person age: "))
if(age5<12):
    amount5 = ticket - (ticket * 30 / 100)
elif (age5 > 59):
    amount5 = ticket - (ticket * 50 / 100)
else:
    amount5 = ticket

total = amount1 + amount2 + amount3 + amount4 + amount5

print("Total ticket amount =", total)



