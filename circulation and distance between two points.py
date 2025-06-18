x= 1
y= 2
z= 3
print("\nbefore circulation: x=", x, ",y=", y, ",z=", z)
x, y, z = z, x, y
print("\nafter crculation: x=", x, ",y=", y, ",z=", z)

# calculate the distance between two points
import math
x1, y1 =0, 0
x2, y2 =3, 4

distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("\nDistance between points(0,0) and (3,4):",distance)
