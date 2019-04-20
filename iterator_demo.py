x = [1, 2, 3]
s = iter(x)

print(next(s))
print(next(s))
print(next(s))


y = [i*5 for i in x]
print(y)
