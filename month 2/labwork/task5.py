def coordinate_proper(border_x,house_x,border_y,house_y):
    coordinates = {
    'border_x': 0,
    'border_y': 0,
    'house_x': 0,
    'house_y': 0
    }
    coordinates["border_x"] = border_x  
    coordinates["border_y"] = border_y 
    coordinates["house_x"] = house_x
    coordinates["house_y"] = house_y
    return coordinates
    
def nlogonia_position(coordinates):
    border_x = coordinates["border_x"]
    border_y = coordinates["border_y"]
    house_x = coordinates["house_x"]
    house_y = coordinates["house_y"]
    if projection(border_x,house_x) == 0 or projection(border_y,house_y) == 0:
        print("border")
    else:
        if (projection(border_x,house_x) == 1 and projection(border_y,house_y) == 1):
            print("NE")
        if (projection(border_x,house_x) == 1 and projection(border_y,house_y) == -1):
            print("SW") 
        if (projection(border_x,house_x) == -1 and projection(border_y,house_y) == 1):
            print("NW")
        if (projection(border_x,house_x) == 1 and projection(border_y,house_y) == 1):
            print("SE")

def projection(border, house):
    if house == border:
        return 0
    elif house > border:
        return 1
    else:
        return -1

print("Введите x координату границы:")
border_x = int(input())
print("Введите y координату границы:")
border_y = int(input())
print("Введите x координату дома:")
house_x = int(input())
print("Введите y координату дома:")
house_y = int(input())
nlogonia_position(coordinate_proper(border_x,house_x,border_y,house_y))