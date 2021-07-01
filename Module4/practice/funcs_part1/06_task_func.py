# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    if (x - xc)**2 + (y - yc)**2 < r**2:
        return (x - xc)**2 + (y - yc)**2 < r**2
    return (x - xc)**2 + (y - yc)**2 < r**2


print(point_in_circle(2, 2, 1, 1, 10))
print(point_in_circle(1, 1, 2, 2, 0.25))
