class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)
    
    def __mul__(self, other):
        self.x *= other
        self.y *= other
        return Vector(self.x, self.y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)
    
    def __mult__(self, other):
        self.x *= other.x,
        self.y *= other.y,
        return Point(self.x, self.y)