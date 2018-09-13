import sys, random
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