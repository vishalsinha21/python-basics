class RadiusInputError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class Circle:

    def __init__(self, radius):
        if not isinstance(radius, int):
            raise RadiusInputError("'" + radius + "' is not a number")
        self.radius = radius


cir = Circle(10)
print(cir.radius)
