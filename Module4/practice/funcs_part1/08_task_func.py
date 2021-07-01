# Напишите функцию находящую n-ое число Фибоначчи.

n = int(input())

def fibonachi(n):
    i = 0
    fib1 = 1
    fib2 = 1
    while i < n - 2:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        i += 1
    return fib2

print(fibonachi(n))
