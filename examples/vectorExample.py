import sys, random
sys.path.insert(0, r'.\libs')
from vector import *

v1 = Vector(6, 7, 5)
print(v1.mag)
v2 = Vector(4, 3, 2)
v3 = v2 + v1
print(v3)
v3 += v1
print(v3)