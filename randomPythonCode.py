import math
import django
def areaOfCircle(radius):
    return math.pi*(int(radius)*int(radius))
rad = input('User enter radius of circle :')
area = areaOfCircle(rad)
print('area of circle with radius {0} is {1:.3f}'.format(rad , area))