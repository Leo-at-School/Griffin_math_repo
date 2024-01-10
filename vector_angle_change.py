from math import atan, pi

solution = []

#Example point 1
p1_x = -2.224
p1_y = -6.8341
#Example point 2
p2_x = 2.6
p2_y = 5.3225

#Points as a slope
slope_1 = p1_y/p1_x
slope_2 = p2_y/p2_x

angle_1 = (180/pi) * atan(slope_1)
angle_2 = (180/pi) * atan(slope_2)

if angle_1 < 0:
    angle_1 = -1 * angle_1 + 90

elif p1_y < 0:
    angle_1 += 180

if angle_2 < 0:
    angle_2 = -1 * angle_2 + 90

elif p2_y < 0:
    angle_2 += 180

solution.append(angle_1)
solution.append(angle_2)

print()
print("point 1: (" + str(p1_x) + "," + str(p1_y) + ") ⇒ " + str(solution[0]) + " degrees off the x axis")
print("Point 2: (" + str(p2_x) + "," + str(p2_y) + ") ⇒ " + str(solution[1]) + " degrees off the x axis")
print()
print("Point 2 is rotated " + str(solution[1] - solution[0]) + " degrees relative to point 1")
