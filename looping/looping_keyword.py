#1. pass: neglect expected indentation error. / It is used to skip the execution of the loop body for a particular iteration.
for i in range(1, 10):
    pass


#2. break: For terminating the loop or stop the loop. /  To stop the loop execution when a particular condition is met.
for i in range(1, 10):
    if i == 4:
        break
    print(i)


#3. continue: To stop particular iteration and continue with the next iteration of the loop.
for i in range(1, 10):
    if i == 3:
        continue
    print(i)


#4. else: The else block will be executed when the loop is completed (no break). Agr break use kiya to else block execute nahi hoga.
for i in range(1, 10):
    if i == 4:
        break
    print(i)
else:
    print('else block executed')

                                         #OR

# else: Else will execute when loop executed successfully without any break statement.
for i in range(1, 10):
    if i == 4:
        continue
    print(i)
else:
    print('else block executed')