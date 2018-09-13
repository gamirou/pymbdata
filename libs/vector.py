import random

class Vector:
    """An object that has three attributes, x, y and z coordinates. Useful in graphics, but also maths."""

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def mag(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def copy(self):
        return Vector(self.x, self.y, self.z)
    
    @staticmethod
    def random2D():
        return Vector(random.uniform(0, 1), random.uniform(0, 1))

    @staticmethod
    def random3D():
        return Vector(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

    def __str__(self):
        lst = [self.x, self.z] if self.z == 0 else [self.x, self.y, self.z]
        return str(tuple(lst))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

"""
fromAngle() 	Make a new 2D unit vector from an angle
add() 	Adds x, y, and z components to a vector, one vector to another, or two independent vectors
sub() 	Subtract x, y, and z components from a vector, one vector from another, or two independent vectors
mult() 	Multiply a vector by a scalar
div() 	Divide a vector by a scalar
dist() 	Calculate the distance between two points
dot() 	Calculate the dot product of two vectors
cross() 	Calculate and return the cross product
normalize() 	Normalize the vector to a length of 1
limit() 	Limit the magnitude of the vector
setMag() 	Set the magnitude of the vector
heading() 	Calculate the angle of rotation for this vector
rotate() 	Rotate the vector by an angle (2D only)
lerp() 	Linear interpolate the vector to another vector
angleBetween() 	Calculate and return the angle between two vectors
array() 	Return a representation of the vector as a float array
"""