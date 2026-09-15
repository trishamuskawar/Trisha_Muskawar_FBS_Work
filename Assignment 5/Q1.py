id = "admin"
password = "1234"

count = 0

while count < 3:

    userid = input("Enter userid: ")
    userpassword = input("Enter password: ")

    if (userid == id and userpassword == password):
        print("Login successful")
        break

    else:
        print("Incorrect userid or password")
        count = count + 1

if count == 3:
    print("You have used all 3 attempts. Program terminated.")