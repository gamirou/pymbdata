import random
import math

from .matrix import Matrix


class Vector:
    """An object that has three attributes, x, y and z coordinates. Useful in graphics, but also maths."""

    def __init__(self, x, y=0, z=0):
        """Initializes an vector

        Args:
            x (tuple, list, dict, int, float) : X-coordinate, or a tuple, list or a dictionary representation
            y (int, float, optional)          : Y-coordinate, or None if x is not given as a number
            z (int, float, optional)          : Z-coordinate, or None if x is not given as a number

        Returns:
            None
        """
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
        """Returns the magnitude (length) of the vector"""
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    @property
    def heading(self):
        """Calculate the angle of rotation for this vector"""
        return math.atan(self.y / self.x)

    def copy(self):
        """Returns a coppied vector"""
        return Vector(self.x, self.y, self.z)

    @classmethod
    def random2D(cls):
        """Creates a random 2D vector"""
        return Vector(random.uniform(0, 1), random.uniform(0, 1))

    @classmethod
    def random3D(cls):
        """Creates a random 3D vector"""
        return Vector(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

    @classmethod
    def normalized(cls, other):
        """Creates a new normalized vector"""
        return cls(other.x / other.mag, other.y / other.mag, other.z / other.mag)

    def normalize(self):
        """Normalize the vector to a length of 1 and saves it"""
        self.x /= self.mag
        self.y /= self.mag
        self.z /= self.mag

    def __str__(self):
        """Returns the string representation of a vector"""
        lst = [self.x, self.y] if self.z == 0 else [self.x, self.y, self.z]
        return str(tuple(lst))

    def __add__(self, other):
        """Adds two vectors together

        Args:
            other (int, float, tuple, list, Vector) : The other vector

        Returns:
            Vector - Vector after operation is done 
        """
        newX, newY, newZ = 0, 0, 0
        if isinstance(other, (int,float)):
            newX = self.x + other
            newY = self.y + other
            if self.z != 0:
                newZ = self.z + other
        elif isinstance(other, (tuple, list)):
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
        """Incrementing addition of two vectors

        Args:
            other (int, float, tuple, list, Vector) : The other vector

        Returns:
            None - it changes the attributes of self
        """
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
        """Substracts two vectors together

        Args:
            other (int, float, tuple, list, Vector) : The other vector

        Returns:
            Vector - Vector after operation is done 
        """
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
        """Multiplies two vectors together

        Args:
            other (int, float, tuple, list, Vector) : The other vector

        Returns:
            Vector - Vector after operation is done 
        """
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
        """Make a new 2D unit vector from an angle"""
        if type_ == "degrees":
            angle = math.radians(angle)
        else:
            raise TypeError("The only accepted types are degrees and radians")

        return cls(math.cos(angle), math.sin(angle))

    @staticmethod
    def dist(vec1, vec2):
        """Calculate the distance between two points"""
        return ((vec1.x - vec2.x) ** 2 + (vec1.y - vec2.y) ** 2 + (vec1.z - vec2.z) ** 2) ** 0.5

    def setMag(self, new):
        """Set the magnitude of the vector"""
        change = new / self.mag
        self.x *= change
        self.y *= change
        self.z *= change

    def toList(self):
        """Return a representation of the vector as a list"""
        output = [self.x, self.y]
        if self.z != 0:
            output.append(self.z)

        return output

    def toTuple(self):
        """Return a representation of the vector as a tuple"""
        return tuple(self.toList())

    def toDict(self):
        """Return a representation of the vector as a dictionary"""
        output = {"x": self.x, "y": self.y}
        if self.z != 0:
            output["z"] = self.z

        return output

    def dot(self, other):
        """Calculate the dot product of two vectors"""
        return (self.x * other.x) + (self.y * other.y)

    def angleBetween(self, other):
        """Calculate and return the angle between two vectors"""
        return math.acos(self.dot(other) / (self.mag * other.mag))

    def cross(self, other):
        """Calculate and return the cross product of two vectors"""
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)

    @classmethod
    def rotated(cls, other, angle, type_="radians"):
        """Returns a copy of a rotated vector"""
        vector = other.copy()
        vector.rotate(angle, type_)
        return vector

    def rotate(self, angle, type_="radians"):
        """Rotate the vector by an angle (2D only)"""
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

    def lerp(self, other, ratio):
        """Linear interpolate the vector to another vector"""
        first_half = self.__mul__(1 - ratio)
        second_half = other.__mul__(ratio)
        return first_half.__mul__(second_half)

    def limit(self, maxMag):
        """Limit the magnitude of the vector"""
        if self.mag > maxMag:
            self.normalize()
            self.setMag(maxMag)

# This is where we add unit vectors
UNIT = {
    "i": Vector(1, 0, 0),
    "j": Vector(0, 1, 0),
    "k": Vector(0, 0, 1)
}

"""
TODO in future versions
slerp() 	Spherical interpolate the vector to another vector
nlerp() 	Normalized linear interpolate the vector to another vector
"""
