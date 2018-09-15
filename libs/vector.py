import random
import math

from matrix import *


class Vector:
    """An object that has three attributes, x, y and z coordinates. Useful in graphics, but also maths."""

    def __init__(self, x, y=0, z=0):
        if isinstance(x, (tuple, list)):
            if len(x) >= 2 and len(x) < 4:
                self.x = x[0]
                self.y = x[1]
                if len(x) == 3:
                    self.z = x[2]
            else:
                raise AttributeError("Length of list has to be 2 or 3")
        elif isinstance(x, dict):
            self.x = x['x']
            self.y = x['y']
            if x['z'] is not None:
                self.z = x['z']
        elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise AttributeError("Your arguments are invalid")

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

    @classmethod
    def normalized(cls, other):
        """Creates a new normalized vector"""
        return cls(other.x / other.mag, other.y / other.mag, other.z / other.mag)

    def normalize(self):
        """Normalizes the current vector and saves it"""
        self.x /= self.mag
        self.y /= self.mag
        self.z /= self.mag

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
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

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
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    def __sub__(self, other):
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, int) or isinstance(other, float):
            newX = self.x - other
            newY = self.y - other
            if self.z != 0:
                newZ = self.z - other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    newX = self.x - other[0]
                    newY = self.y - other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    newX = self.x - other[0]
                    newY = self.y - other[1]
                    newZ = self.z - other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            newX = self.x - other.x
            newY = self.y - other.y
            newZ = self.z - other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return Vector(newX, newY, newZ)

    def __isub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x -= other
            self.y -= other
            if self.z != 0:
                self.z -= other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    self.x -= other[0]
                    self.y -= other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    self.x -= other[0]
                    self.y -= other[1]
                    self.z -= other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    def __mul__(self, other):
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, int) or isinstance(other, float):
            newX = self.x * other
            newY = self.y * other
            if self.z != 0:
                newZ = self.z * other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    newX = self.x * other[0]
                    newY = self.y * other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    newX = self.x * other[0]
                    newY = self.y * other[1]
                    newZ = self.z * other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            newX = self.x * other.x
            newY = self.y * other.y
            newZ = self.z * other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return Vector(newX, newY, newZ)

    def __imul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x *= other
            self.y *= other
            if self.z != 0:
                self.z *= other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    self.x *= other[0]
                    self.y *= other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    self.x *= other[0]
                    self.y *= other[1]
                    self.z *= other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    def __div__(self, other):
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, int) or isinstance(other, float):
            newX = self.x / other
            newY = self.y / other
            if self.z != 0:
                newZ = self.z / other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    newX = self.x / other[0]
                    newY = self.y / other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    newX = self.x / other[0]
                    newY = self.y / other[1]
                    newZ = self.z / other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            newX = self.x / other.x
            newY = self.y / other.y
            newZ = self.z / other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return Vector(newX, newY, newZ)

    def __idiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x /= other
            self.y /= other
            if self.z != 0:
                self.z /= other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    self.x /= other[0]
                    self.y /= other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    self.x /= other[0]
                    self.y /= other[1]
                    self.z /= other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    def __floordiv__(self, other):
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, int) or isinstance(other, float):
            newX = self.x // other
            newY = self.y // other
            if self.z != 0:
                newZ = self.z // other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    newX = self.x // other[0]
                    newY = self.y // other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    newX = self.x // other[0]
                    newY = self.y // other[1]
                    newZ = self.z // other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            newX = self.x // other.x
            newY = self.y // other.y
            newZ = self.z // other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return Vector(newX, newY, newZ)

    def __ifloordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x //= other
            self.y //= other
            if self.z != 0:
                self.z //= other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    self.x //= other[0]
                    self.y //= other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    self.x //= other[0]
                    self.y //= other[1]
                    self.z //= other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            self.x //= other.x
            self.y //= other.y
            self.z //= other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    def __pow__(self, other):
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, int) or isinstance(other, float):
            newX = self.x ** other
            newY = self.y ** other
            if self.z != 0:
                newZ = self.z ** other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    newX = self.x ** other[0]
                    newY = self.y ** other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    newX = self.x ** other[0]
                    newY = self.y ** other[1]
                    newZ = self.z ** other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            newX = self.x ** other.x
            newY = self.y ** other.y
            newZ = self.z ** other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return Vector(newX, newY, newZ)

    def __ipow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x **= other
            self.y **= other
            if self.z != 0:
                self.z **= other
        elif isinstance(other, tuple) or isinstance(other, list):
            # If 2D vector
            if self.z == 0:
                if len(other) == 2:
                    self.x **= other[0]
                    self.y **= other[1]
                else:
                    raise ValueError("Your list has to be of length 2.")
            # If 3D vector
            else:
                if len(other) == 3:
                    self.x **= other[0]
                    self.y **= other[1]
                    self.z **= other[2]
                else:
                    raise ValueError("Your list has to be of length 3.")
        elif isinstance(other, Vector):
            self.x **= other.x
            self.y **= other.y
            self.z **= other.z
        else:
            raise TypeError(
                "Your input has to be a vector, a scalar, a list or a tuple.")

        return self

    @classmethod
    def fromAngle(cls, angle, type_="radians"):
        if type_ == "degrees":
            angle = math.radians(angle)
        else:
            raise TypeError("The only accepted types are degrees and radians")

        return cls(math.cos(angle), math.sin(angle))

    @staticmethod
    def dist(vec1, vec2):
        return ((vec1.x - vec2.x) ** 2 + (vec1.y - vec2.y) ** 2 + (vec1.z - vec2.z) ** 2) ** 0.5

    def setMag(self, new):
        change = new / self.mag
        self.x *= change
        self.y *= change
        self.z *= change

    def toList(self):
        output = [self.x, self.y]
        if self.z != 0:
            output.append(self.z)

        return output

    def toTuple(self):
        return tuple(self.toList())

    def toDict(self):
        output = {"x": self.x, "y": self.y}
        if self.z != 0:
            output["z"] = self.z

        return output

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y)

    def angleBetween(self, other):
        return math.acos(self.dot(other) / (self.mag * other.mag))

    def cross(self, other):
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    @classmethod
    def rotated(cls, other, angle, type_="radians"):
        vector = other.copy()
        vector.rotate(angle, type_)
        return vector

    def rotate(self, angle, type_="radians"):
        if type_ in ("radians", "degrees") and self.z == 0:
            if type_ == "degrees":
                angle = math.radians(angle)
                print(angle)

            angle_cos = math.cos(angle)
            angle_sin = math.sin(angle)

            self.x = angle_cos * self.x - angle_sin * self.y
            self.y = angle_sin * self.x + angle_cos * self.y
        else:
            raise ValueError("The only types accepted are radians and degrees.")

    @property
    def heading(self):
        return math.atan(self.y / self.x)

    def lerp(self, other, ratio):
        first_half = self.__mul__(1 - ratio)
        second_half = other.__mul__(ratio)
        return first_half.__mul__(second_half)


# This is where we add unit vectors
UNIT = {
    "i": Vector(1, 0, 0),
    "j": Vector(0, 1, 0),
    "k": Vector(0, 0, 1)
}

"""
TODO:

limit() 	Limit the magnitude of the vector

TODO in future versions
slerp() 	Spherical interpolate the vector to another vector
nlerp() 	Normalized linear interpolate the vector to another vector
"""
