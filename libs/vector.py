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
    
    @classmethod
    def random2D(cls):
        return Vector(random.uniform(0, 1), random.uniform(0, 1))

    @classmethod
    def random3D(cls):
        return Vector(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

    # @classmethod
    # def normalize(cls, other):
    #     return cls(other.x / other.mag, other.y / other.mag, other.z / other.mag)

    # def normalize(self):
    #     self.x /= self.mag
    #     self.y /= self.mag
    #     self.z /= self.mag

    def __str__(self):
        lst = [self.x, self.y] if self.z == 0 else [self.x, self.y, self.z]
        return str(tuple(lst))

    def __add__(self, other):
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, int) or isinstance(other, float):
            newX = self.x + other
            newY = self.y + other
            if self.z != 0:
                newZ = self.z + other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    newX = self.x + other[0]
                    newY = self.y + other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    newX = self.x + other[0]
                    newY = self.y + other[1]
                    newZ = self.z + other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            newX = self.x + other.x
            newY = self.y + other.y
            newZ = self.z + other.z
        else:
            raise TypeError("Your input has to be a vector, a scalar, a list or a tuple.")

        return Vector(newX, newY, newZ)

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x += other
            self.y += other
            if self.z != 0:
                self.z += other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    self.x += other[0]
                    self.y += other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    self.x += other[0]
                    self.y += other[1]
                    self.z += other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            raise TypeError("Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    # def __sub__(self, other):
    #     return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # def __isub__(self, other):
    #     self.x -= other.x
    #     self.y -= other.y
    #     self.z -= other.z
    #     return self
    

"""
normalize()
fromAngle() 	Make a new 2D unit vector from an angle
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