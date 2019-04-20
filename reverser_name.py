name = input('Whats your name? ')

names = name.split(' ')

for n in names:
    print(n[::-1], end =' ')
