from collections import deque


hex_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                   '8': 8, '9': 9, 'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12,
                   'D': 13, 'd': 13, 'E': 14, 'e': 14, 'F': 15, 'f': 15,
                   0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
                   }

number_1 = list(input('Введите 1-е шестнадцатеричное число: '))
number_2 = list(input('Введите 2-е шестнадцатеричное число: '))
numbers_summ = deque()
s = 0
q = 0

l1 = len(number_1)
l2 = len(number_2)

for i in range(l1):
    if number_1[i].isdigit():
        pass
    else:
        number_1[i] = hex_numbers[number_1[i]]
print(number_1)

for i in range(l2):
    if number_2[i].isdigit():
        pass
    else:
        number_2[i] = hex_numbers[number_2[i]]
print(number_2)

l = max(l1, l2)

if l1 == l2:
    for i in range(l1 - 1, -1, -1):
        s = int(number_1[i]) + int(number_2[i])
        if s > 16:
            s -= 16
            numbers_summ.appendleft(s)
            numbers_summ.appendleft(1)
        else:
            numbers_summ.appendleft(s)
elif l1 > l2:
    for i in range(l1 - 1, 0, -1):
        s = int(number_1[i]) + int(number_2[i-1])
        if s > 16:
            s -= 16
            numbers_summ.appendleft(s)
            q = int(number_1[i-1]) + 1 + int(number_2[i-2])
            numbers_summ.appendleft(q)
    numbers_summ.appendleft(number_1[0])
else:
    for i in range(l2 - 1, 0, -1):
        s = int(number_2[i]) + int(number_1[i-1])
        if s > 16:
            s -= 16
            numbers_summ.appendleft(s)
            q = int(number_2[i-1]) + 1 + int(number_1[i-2])
            numbers_summ.appendleft(q)

       
        numbers_summ.appendleft(number_2[0])

print(numbers_summ)

for i in range(len(numbers_summ)):
    if numbers_summ[i] > 9:
        numbers_summ[i] = hex_numbers[numbers_summ[i]]

print(numbers_summ)