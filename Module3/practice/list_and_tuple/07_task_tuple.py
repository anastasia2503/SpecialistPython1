# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here
tup = (2, 4, 6, -4, 12, 0, 5)
x = 0
for el in tup:
    if el > x:
        x = el
    else:
        x = x
print(x)
