import math
# u"\u00b0"
def find_Angle(AB, BC):
    return math.degrees(math.atan(BC/AB))
AB = int(input())
BC = int(input())
print(str(round(find_Angle(BC, AB))) + u"\u00b0")


