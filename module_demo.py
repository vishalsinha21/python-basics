import itertools

n = [10, 13, 16, 22, 9, 4 , 37]
even = []
odd = []

for key, grp in itertools.groupby(n, key=lambda i:i%2 == 0):
    if key:
        even.extend(grp)
    else:
        odd.extend(grp)

print(even)
print(odd)            
