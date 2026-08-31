#WAP to calculate selling price of book based on cost price and discount.

basic = int(input('Enter the basic salary: '))

da = basic * 10/100
ta = basic * 12/100
hra = basic * 15/100
total_salary = basic + da + ta + hra

print(f'{total_salary} is the total salary of employee.')