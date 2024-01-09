from math import sqrt, asin

#point 1
p1_x = 3
p1_y = 4
#point 2
p2_x = 6
p2_y = 10

#points as a slope
slope_1 = p1_y/p1_x
slope_2 = p2_y/p2_x

#Finding angle rotation (in radians)
k1 = (slope_1 ** 2) + 1
k2 = (slope_2 ** 2) + 1

angle_1 = asin(sqrt(k1)/k1)
angle_2 = asin(sqrt(k2)/k2)

rotation = angle_2 - angle_1

#Printing
print("(" + str(p1_x) + "," + str(p1_y) + ") to (" + str(p2_x) + "," + str(p2_y) + ")")
print("rotation: " + str(rotation))


