import math

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'point : ({}, {}, {})'.format(self.x, self.y, self.z)

    def distance(self, other):
        return math.sqrt( (self.x-other.x)**2 + (self.y-other.y)**2 + (self.z -other.z)**2 )

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

p1 = Point(4, 5, 6)
p2 = Point(-2, -1, 4)

print(p1)
print(p2)
print(p1.distance(p2))

print(p1 + p2)
