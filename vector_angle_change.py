from math import atan, pi

solution = []

#Example point 1
x1 = -2
y1 = 5
#Example point 2
x2 = 5
y2 = 2

#Point 1 pre-processing
if x1 == 0 and y1 > 0:
    angle_1 = pi/2
    
elif x1 == 0 and y1 < 0:
    angle_1 = -pi/2

elif (x1 > 0 and y1 == 0) or (x1 == 0 and y1 == 0):
    angle_1 = 0
    
elif x1 < 0 and y1 == 0:
    angle_1 = pi

else:
    slope_1 = y1/x1

#Point 2 pre-processing
if x2 == 0 and y2 > 0:
    angle_2 = pi/2
    
elif x2 == 0 and y2 < 0:
    angle_2 = -pi/2
    
elif  (x2 > 0 and y2 == 0) or (x2 == 0 and y2 == 0):
    angle_2 = 0
    
elif x2 < 0 and y2 == 0:
    angle_2 = pi
    
else:
    slope_2 = y2/x2

#Angle off x axis for point 2
if x1 > 0 and y1 > 0:
    angle_1 = atan(slope_1)
    
elif x1 < 0 and y1 > 0:
    angle_1 = pi - atan(abs(slope_1))
    
elif x1 < 0 and y1 < 0:
    angle_1 = ((3*pi)/2) - atan(slope_1)
    
elif x1 > 0 and y1 < 0:
    angle_1 = (2*pi) - atan(abs(slope_1))

#Angle off x axis for point 2
if x2 > 0 and y2 > 0:
    angle_2 = atan(slope_2)
    
elif x2 < 0 and y2 > 0:
    angle_2 = pi - atan(abs(slope_2))
    
elif x2 < 0 and y2 < 0:
    angle_2 = ((3*pi)/2) - atan(slope_2)
    
elif x2 > 0 and y2 < 0:
    angle_2 = (2*pi) - atan(abs(slope_2))

#Convert to degrees
angle_1 *= (180/pi)
angle_2 *= (180/pi)

#Find how much each is rotated (+ rotation: clockwise, - rotation: counterclockwise)
angle_difference = angle_2 - angle_1

print()
print("point 1: (" + str(x1) + "," + str(y1) + ") ⇒ " + str(angle_1) + " degrees off the x axis")
print("Point 2: (" + str(x2) + "," + str(y2) + ") ⇒ " + str(angle_2) + " degrees off the x axis")
print()
print("Point 2 is rotated " + str(angle_difference) + " degrees relative to point 1")
