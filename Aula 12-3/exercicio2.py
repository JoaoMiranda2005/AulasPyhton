
a = [2, 3, 4, 5, 6]

b = [x ** 2 for x in a if x % 2 == 0 and x % 8 == 0]

print(b)
