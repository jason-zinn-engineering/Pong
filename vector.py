import math

class vector:
    def __init__(self):
        pass

    # Initializer / Instance Attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length()
        return math.sqrt(x*x + y*y)

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other);
        return self.x*other.x + self.y*other.y