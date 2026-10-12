str = "Python"
n = 2
str1 = ""
for i in range(0, len(str)):
    if (i != n):
        str1 = str1 + str[i]
    else:
        pass
print(str1)