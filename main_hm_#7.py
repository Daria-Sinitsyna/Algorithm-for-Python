import random

print('Задание №1')
"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). 
Выведите на экран исходный и отсортированный массивы. 
Сортировка должна быть реализована в виде функции. 
По возможности доработайте алгоритм (сделайте его умнее).
"""
def buble(list):
    n = 1
    while n < len(list):
        i = 0
        for i in range(len(list) - n):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

        n += 1

massive_1 = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]
print(f'Исходный массив: {massive_1}')
buble(massive_1)
print(f'Отсортированный массив: {massive_1}')

print('Задание №2')
"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, 
то используйте метод сортировки, который не рассматривался на уроках
"""
m = int(input('Введите m: '))
massive_2 = [random.randint(-100, 100) for _ in range(0, 2*m + 1)]
print(f'Изначальный массив: {massive_2}')
n = len(massive_2)
massive_2_sorted = [0]*n
mediana = 0
# очень быстрый читерский вариант
massive_2 = sorted(massive_2)
mediana = massive_2[m]
print(f'отсортированный массив: {massive_2}\n'
      f'Медиана: {mediana} ')

for i in range(0, n):
    minimum = min(massive_2)
    massive_2_sorted[i] = minimum
    massive_2.pop(massive_2.index(minimum))

mediana = massive_2_sorted[m]
print(f'Отсортированный массив: {massive_2_sorted} \n'
      f'медиана: {mediana}')


print('Задание №3')
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и 
отсортированный массивы.
"""
massive_3 = [random.randint(0, 50) for _ in range(random.randint(0, 20))]
print(f'Исходный массив: {massive_3}')

def merge_sort(a):

    if len(a) <= 1:
        return a
    mid = len(a) // 2

    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])

    return merge(left, right, a.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

print(merge_sort(massive_3))