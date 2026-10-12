str1 = "banana"
str2 = ""

for i in str1:
    if (i == 'a'):
        str2 = str2 + '$'
    else:
        str2 = str2 + i

print(str2)