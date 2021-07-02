# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

a = 3443
b = 7777


def palindrome(a, b):
    number = a
    res = 0
    while number <= b:
        n_number = str(number)
        rev_number = n_number[::-1]
        if rev_number == n_number:
            res += 1
        number += 1
    return res


print(palindrome(a, b))
