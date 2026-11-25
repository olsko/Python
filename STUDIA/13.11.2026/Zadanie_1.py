import math

def distance(p1,p2):

    if len(p1) > 3 or len(p1) < 2 :
        d = "nieprawidłowa ilość punktów"
    
    elif len(p1) == 2:
        d = math.sqrt( ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))
    
    else:
        d = math.sqrt( ((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2) + ((p2[2] - p1[2]) ** 2))
    
    return d


print(distance((1,2), (4,6)))


print(distance((1,2,3), (4,6,3)))