a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    print('треугольник существует.')
else:
    print('треугольник не существует.')

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance1 = (x1**2 + y1**2)**0.5
distance2 = (x2**2 + y2**2)**0.5
if distance1 < distance2:
    print(f'точка M1({x1}, {y1}) ближе к началу координат.')
else:
    print(f'точка M2({x2}, {y2}) блиэе к началу координат. ')

import math
a = float(input())
r = float(input())
square_area = a**2
circle_area = math.pi * r**2
if square_area > circle_area:
    print('квадрат имеет бОльшую площадь:', square_area)
else:
    print('круг имеет бОльшую площадь:', circle_area)




