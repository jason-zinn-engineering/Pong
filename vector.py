import math

class vector:
    def __init__(self):
        self.x = 0
        self.y = 0
        pass

    # Initializer / Instance Attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Cartesian length of the vector
    def length():
        return math.sqrt(x*x + y*y)

    # Vector addition
    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    # Vector subtraction
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    # dot product
    def __mul__(self, other):
        return self.x*other.x + self.y*other.y