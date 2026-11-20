# def genNo():
#     a = 10
#     b = a
#     a += 1
#     return b
# print(genNo())

def genNo():
    #return [i for i in range(1, 11)]
    for i in range(1, 100):
        yield(i)
d = genNo()
print(next(d))
print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# print(next(d))