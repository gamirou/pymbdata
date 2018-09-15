import sys, random, math
sys.path.insert(0, r'.\libs')
from matrix import *

matrix = Matrix([[6, 1, 1], 
                 [4, -2, 5], 
                 [2, 8, 7]])

print(matrix.determinant)
