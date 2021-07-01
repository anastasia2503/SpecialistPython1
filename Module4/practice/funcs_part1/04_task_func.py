# Даны координаты трех точек p1(x1; y1) p2(x2; y2) p3(x3; y3).
# Напишите функцию, проверябщую можно ли построить треугольник, соединив данные точки отрезками

def can_triangle(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    lenght12 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    lenght13 = ((x3 - x1)**2 + (y3 - y1)**2)**0.5
    lenght23 = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
    if lenght13 + lenght23 < lenght12 and lenght12 + lenght13 < lenght23 and lenght23 + lenght12 < lenght13:
        return lenght13 + lenght23 < lenght12
    return lenght13 + lenght23 < lenght12

# Пример вызова функции
print(can_triangle((10, 12), (14, 18), (12, 12)))
