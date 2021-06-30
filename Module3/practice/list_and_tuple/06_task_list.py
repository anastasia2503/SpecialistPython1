# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
a = []
x = first_number
while x <= second_number:
    a.append(x)
    x += 1

n = []
for el in a:
    if el % 3 == 0:
        n.append(el)
print(n)
