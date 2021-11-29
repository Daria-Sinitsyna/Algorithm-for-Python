import random

print('Задание №1')
"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
result = {}

for i in range(2, 10):
    result[i] = []
    for j in range(2, 100):
        if j % i == 0:
            result[i].append(j)
    print(f'Для числа {i} кратны - {len(result[i])} чисел/числа. Кратные числа: {result[i]}. \n')

print('Задание №2')
"""
Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив 
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
т.к. именно в этих позициях первого массива стоят четные числа.
"""
massive_1 = input('Введите массив чисел через запятую: ').split(',')
l = len(massive_1)
massive_2 = []

for i in range(0, l - 1):
    if massive_1[i].isdigit():
        pass
    else:
        print(f'{massive_1[i]} не число')
        massive_1.remove(massive_1[i])

for i in range(0, l - 1):
    if int(massive_1[i]) % 2 == 0:
        massive_2.append(massive_1.index(massive_1[i]))
    else:
        print(f'{massive_1[i]} нечетное число')

print(f'Введенный массив чисел {massive_1}, массив индексов четных чисел {massive_2} \n')

print('Задание №3')
"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
massive_3 = [random.randint(0, 100) for _ in range(random.randint(1, 20))]
print(f'Изначальный массив: {massive_3} \n')

maximum = massive_3[0]
minimum = massive_3[0]

for i in massive_3:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i
index_max = massive_3.index(maximum)
index_min = massive_3.index(minimum)

massive_3[index_max], massive_3[index_min] = massive_3[index_min], massive_3[index_max]
print(f'Массив после перестановки элементов: {massive_3}')

print('Задание №4')
"""
Определить, какое число в массиве встречается чаще всего.
"""
massive_4 = [random.randint(0, 10) for _ in range(random.randint(1, 20))]
print(f'Изначальный массив: {massive_4}')

element = 0
number = ' '

for i in massive_4:
    if massive_4.count(i) > 1 and massive_4.count(i) > element:
        element = massive_4.count(i)
        number = i

print(f'Чаще всего в массиве встречается число: {number}, {element} раз(а) \n')

print('Задание №5')
"""
В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию (индекс) в массиве.
"""
massive_5 = [random.randint(-50, 50) for _ in range(random.randint(1, 20))]
print(f'Изначальный массив: {massive_5}')
index_neg_element = -1

for i in massive_5:
    if i < 0 and index_neg_element == -1:
        index_neg_element = massive_5.index(i)
    elif i < 0 and i > massive_5[index_neg_element]:
        index_neg_element = massive_5.index(i)

print(f'Максимальный отрицательный элемент в массиве: {massive_5[index_neg_element]}')

print('Задание №6')
"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""
massive_6 = [random.randint(0, 10) for _ in range(random.randint(1, 20))]
print(f'Изначальный массив: {massive_6}')

max_element = massive_6[0]
min_element = massive_6[0]
summ = 0

for i in massive_6:
    if i > max_element:
        max_element = i
    elif i < min_element:
        min_element = i


max_index = massive_6.index(max_element)
min_index = massive_6.index(min_element)

if min_index > max_index:
    min_index, max_index = max_index, min_index

if (max_index - min_index) == 1:
    print('Сумма элементов равна: 0 \n')

for j in range(min_index + 1, max_index):
    summ += massive_6[j]

print(f'максиальный элемент: {max_element}, минимальный элемент: {min_element}, сумма между максимальным и минимальными элементами: {summ} \n')

print('Задание №7')
"""
В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться. 
"""
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

print('Задание №8')
"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
Программа должна вычислять сумму введенных элементов каждой строки и записывать 
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
row = int(input('Введите количество строк: '))
column = int(input('Введите количество столбцов: '))

matrix = []

for i in range(row):
    summ = 0
    a = []
    for j in range(column - 1):
        a.append(int(input(f'строка {i + 1} столбец {j + 1}:  ')))
        summ += a[j]
    a.append(summ)
    matrix.append(a)

for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()

print('Задание №9')
"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
row = int(input('Введите количество строк: '))
column = int(input('Введите количество столбцов: '))

matrix_1 = []

for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input(f'строка {i + 1} столбец {j + 1}:  ')))
    matrix_1.append(a)


b = []
for i in range(row):
    min_el = matrix_1[i][j]
    for j in range(column):
        if matrix_1[i][j] < min_el:
            min_el = matrix_1[i][j]
        print(matrix_1[i][j], end=" ")
    b.append(min_el)
    print()
b.sort(reverse=True)
print(f'Максимальный элемент из минимальных в матрице: {b[0]}')
