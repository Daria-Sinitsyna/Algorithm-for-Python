import cProfile

print('Задание №1')
"""
Проанализировать скорость и сложность одного любого алгоритма, разработанных 
в рамках практического задания первых трех уроков.
"""
import random
"""
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться. 
"""
def massive():
    massive_7 = [random.randint(0, 20) for _ in range(random.randint(2, 20))]
    print(f'Изначальный массив: {massive_7}')

    min_1 = massive_7[0]
    min_2 = massive_7[0]

    massive_7.sort()
    print(f'Отсортированный массив: {massive_7}')

    for k in range(0, (len(massive_7) - 2)):
        if massive_7[k + 1] == massive_7[k]:
            massive_7[k], massive_7[k + 1] = massive_7[k + 1], massive_7[k + 2]

    print(f'Первое минимальное число: {massive_7[0]}, второе минимальное число: {massive_7[1]}')

cProfile.run('massive()')

"""
89 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       14    0.000    0.000    0.000    0.000 random.py:200(randrange)
       14    0.000    0.000    0.000    0.000 random.py:244(randint)
       14    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
        1    0.000    0.000    0.000    0.000 test.py:7(massive)
        1    0.000    0.000    0.000    0.000 test.py:8(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       14    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       23    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
"""

print('Задание №2')
"""
Написать два алгоритма нахождения i-го по счёту простого числа.
"""

# - Без использования Решета Эратосфена;
def without_Eratosfen(n):
    numbers = []
    numbers_sorted = []

    for i in range(100):
        numbers.append(i)
    print(numbers)

    for i in range(2, len(numbers) + 1):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                numbers_sorted.append(i)
                break

    print(f'{n}-е по счету простое число - {numbers_sorted[n]}')


cProfile.run("without_Eratosfen(int(input('Введите i-е по счёту число: ')))")
"""
160 function calls in 3.911 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.911    3.911 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1    0.000    0.000    0.000    0.000 test.py:3(without_Eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    3.911    3.911 {built-in method builtins.exec}
        1    3.910    3.910    3.910    3.910 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      149    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Массив из 100 чисел. Поиск 8го по счету числа. 160 function calls in 3.911 seconds
Массив из 1000 чисел. Поиск 8го по счету числа. 1510 function calls in 2.070 seconds
Массив из 10000 чисел. Поиск 8го по счету числа. 15010 function calls in 1.803 seconds
Массив из 10000 чисел. Поиск 8го по счету числа. 150010 function calls in 1.977 seconds        

"""

# - Использовать алгоритм решето Эратосфена.
def with_Eratosfen(n):
    numbers = []

    for i in range(100000):
        numbers.append(i)

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
        if i != 0:
            numbers_sorted.append(i)

    print(f'{n}-е по счету простое число - {numbers_sorted[n]}')

cProfile.run("with_Eratosfen(int(input('Введите i-е по счёту число: ')))")

"""
8-е по счету простое число - 19
         4932213 function calls in 4.920 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.011    0.011    4.920    4.920 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1    2.028    2.028    2.722    2.722 test.py:3(with_Eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    4.920    4.920 {built-in method builtins.exec}
        1    2.187    2.187    2.187    2.187 {built-in method builtins.input}
  3853705    0.548    0.000    0.548    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1078499    0.146    0.000    0.146    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
"""
900-е по счету простое число - 6997
         4932213 function calls in 5.680 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.011    0.011    5.680    5.680 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        1    2.018    2.018    2.691    2.691 test.py:3(with_Eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    5.680    5.680 {built-in method builtins.exec}
        1    2.977    2.977    2.977    2.977 {built-in method builtins.input}
  3853705    0.528    0.000    0.528    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
  1078499    0.145    0.000    0.145    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
"""
Основное время уходит на создание массива чисел, но мне непонятно на какую строчку ориентироваться в списке профайл. 
Но если ограничить диапазон чисел, то всё происходит быстрее.

Массив из 100 чисел. Поиск 8го по счету числа. 403 function calls in 1.968 seconds
Массив из 1000 чисел. Поиск 8го по счету числа. 4301 function calls in 1.763 seconds
Массив из 10000 чисел. Поиск 8го по счету числа.45536 function calls in 2.368 seconds
Массив из 10000 чисел. Поиск 8го по счету числа. 475999 function calls in 2.503 seconds
"""