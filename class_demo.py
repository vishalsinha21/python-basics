class Person:
    'Person class'

    def __init__(self, fname, lname, age):
        'Person initializer'
        self.fname = fname
        self.lname = lname
        self.age = age

p1 = Person('Vikas', 'Mehta', 32)

print(p1)
print(p1.fname, p1.lname, p1.age)


help(p1)
