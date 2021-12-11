"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.
"""
"""
x86_64 Windows 7
Python 3.8
"""
import sys
"""
Написать два алгоритма нахождения i-го по счёту простого числа.
"""
# - Без использования Решета Эратосфена;
def without_Eratosfen(n):
    numbers = []
    numbers_sorted = []

    for i in range(1000):
        numbers.append(i)
    print(numbers)

    numbers[1] = 0
    for i in range(2, len(numbers) + 1):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            numbers_sorted.append(i)

    size = 0
    size += sys.getsizeof(numbers)
    size += sys.getsizeof(i)
    size += sys.getsizeof(d)
    size += sys.getsizeof(numbers_sorted)

    print(f'Все переменные занимают - {size} байт')

    print(f'{n}-е по счету простое число - {numbers_sorted[n-1]}')

without_Eratosfen(int(input('Введите i-е по счёту число: ')))

"""
Размер массива 100
Все переменные занимают - 608 байт
19-е по счету простое число - 67

Все переменные занимают - 608 байт
20-е по счету простое число - 71

Размер массива 1000
Все переменные занимают - 5256 байт
19-е по счету простое число - 67

Все переменные занимают - 5256 байт
145-е по счету простое число - 829

Увеличивая на порядок размер увеличивается на порядок, самое тяжелое это массив чисел
"""

# - Использовать алгоритм решето Эратосфена.
def with_Eratosfen(n):
    numbers = []

    for i in range(1000):
        numbers.append(i)
    print(numbers)

    numbers[1] = 0

    p = 2
    while p < len(numbers):
        if numbers[p] != 0:
            j = p * 2
            while j < len(numbers):
                numbers[j] = 0
                j = j + p
        p += 1

    numbers_sorted = []

    for i in numbers:
        if numbers[i] != 0:
            numbers_sorted.append(numbers[i])


    print(f'{n}-е по счету простое число - {numbers_sorted[n-1]}')

    size_1 = 0
    size_1 += sys.getsizeof(numbers)
    size_1 += sys.getsizeof(p)
    size_1 += sys.getsizeof(j)
    size_1 += sys.getsizeof(i)
    size_1 += sys.getsizeof(numbers_sorted)

    print(f'Все переменные занимают - {size_1} байт')

with_Eratosfen(int(input('Введите i-е по счёту число: ')))

"""
Размер массива 100
19-е по счету простое число - 67
Все переменные занимают - 620 байт

20-е по счету простое число - 71
Все переменные занимают - 620 байт

Размер массива 1000
19-е по счету простое число - 67
Все переменные занимают - 5268 байт

145-е по счету простое число - 829
Все переменные занимают - 5268 байт
"""