from pymb import Vector

vec1 = Vector(2, 4)
vec2 = Vector.random2D()
vec1 = vec1 + 4
print("Adding with scalar", vec1)
vec1 = vec2 + (2, 4)
print("Adding with tuple", vec1)

vec2 *= (8, 7)
print("Multypling increment by list", vec2) 

vec3 = Vector.from_angle(140, "degrees")
print("Unit vector at 140 degrees", vec3)

vec4 = Vector(3, 3)
print("Heading of vector 4 in degrees is", math.degrees(vec4.heading))

vec5 = Vector(6, 7)
print("Distance between vector 4 and 5 is", Vector.dist(vec4, vec5))
vec5.setMag(10)
print("Magnitude set to 10 on vector 5", vec5)
print("Vector 4 to list", vec4.toList())
print("Vector 4 to dict", vec4.toDict())

normVec = Vector.normalized(vec5)
print("Normalized vector 5 is", normVec)
rotaVec = Vector.rotated(vec4, math.pi/2)
print("Rotated vector 4 by 90 degrees is", rotaVec)

angleBetween45 = vec4.angleBetween(vec5)
print("Angle between vectors 4 and 5 is", math.degrees(angleBetween45))
cross45 = vec4.cross(vec5)
print("Cross product of vectors 4 and 5 is", cross45)
lerp45 = vec4.lerp(vec5, 0.5)
print("Linear interpolation of v4 and 5 at 0.5 is", lerp45)

vec5.limit(4)
print("Vector 5 after being limited to 4", vec5)