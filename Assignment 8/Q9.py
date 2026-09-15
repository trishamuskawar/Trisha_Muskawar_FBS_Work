def palindrome(n):
    temp = n
    rev = 0

    while(n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    if(temp == rev):
        print("Palindrome")
    else:
        print("Not Palindrome")


n = int(input("Enter a number: "))
palindrome(n)