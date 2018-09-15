import sys, random, math
sys.path.insert(0, r'.\libs')
from vector import *

vec1 = Vector(2, 4)
vec2 = Vector.random2D()
vec1 = vec1 + 4
print("Adding with scalar", vec1)
vec1 = vec2 + (2, 4)
print("Adding with tuple", vec1)

vec2 *= (8, 7)
print("Multypling increment by list", vec2) 

vec3 = Vector.fromAngle(140, "degrees")
print("Unit vector at 140 degrees", vec3)

vec4 = Vector(3, 3)
vec5 = Vector(6, 7)
print("Distance between vector 4 and 5 is", Vector.dist(vec4, vec5))
vec5.setMag(10)
print("Magnitude set to 10 on vector 5", vec5)
print("Vector 4 to list", vec4.toList())
print("Vector 4 to dict", vec4.toDict())

angleBetween45 = vec4.angleBetween(vec5)
print("Angle between vectors 4 and 5 is", math.degrees(angleBetween45))