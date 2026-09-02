from math import pi
def area_circle(radius):
    area = pi*(radius**2)
    return area

      
radius = [12, 35, 4]
areas = [0,0,0]
for i in range(len(radius)):
    areas[i] = area_circle(radius[i])
print(areas) 