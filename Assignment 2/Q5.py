#WAP to calculate selling price of book based on cost price and discount.

n1 = int(input('Enter the cost price: '))
n2 = int(input('Enter the discount:'))

discount_amount = n1 * n2/100
selling_price = n1 - discount_amount

print('The selling price of book is: ', selling_price)
