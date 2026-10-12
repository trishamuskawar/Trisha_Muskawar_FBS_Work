li = [10, 39, 20, 47, 87, 70]

even = [0, 0, 0, 0, 0, 0]
odd = [0, 0, 0, 0, 0, 0]

even_count = 0
odd_count = 0

for ind in range(0,6):
    if(li[ind] % 2 == 0):
        even[even_count] = li[ind]
        even_count += 1
    else: 
        odd[odd_count] = li[ind]
        odd_count += 1
print("Even element list: ", even[0:even_count]) # [0:even_count] : yaha ye isiliye likha hai ki agr output me zero nh chahiye to hum ye likh ke print kiya to jitne even elements hai utne hi print honge.
print("Odd element list: ", odd[0:odd_count])
