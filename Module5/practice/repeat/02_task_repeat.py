# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    n_number = str(number)
    rev_number = n_number[::-1]
    if rev_number == n_number:
        return rev_number == n_number
    return rev_number == n_number
