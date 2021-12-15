import hashlib
from collections import Counter

print('Задание №1')
"""
Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""
def str_count(string):
    len_string = len(string)
    hash_set = set()
    h_string = hashlib.sha1(string.encode('utf-8')).hexdigest()

    if len_string > 0:
        for i in range(0, len_string + 1):
            for j in range(i + 2, len_string + 1):
                # print(f'i {i}, j {j} {string[i:j]}')
                h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
                hash_set.add(h)


        return (len(hash_set) - 1)
    else:
        print('Вы не ввели строку')

string_main = input('Введите строку: ').lower()

print(f'Количество различных подстрок в строке {string_main} составляет {str_count(string_main)} \n')

print('Задание №2')
"""
Закодировать любую строку по алгоритму Хаффмана.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes = dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    string_count = Counter(string)

    if len(string_count) <= 1:
        node = Node(None)

        if len(string_count) == 1:
            node.left = Node([key for key in string_count][0])
            node.right = Node(None)

        string_count = {node: 1}

    while len(string_count) != 1:
        node = Node(None)
        spam = string_count.most_common()[:-3:-1]

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del string_count[spam[0][0]]
        del string_count[spam[1][0]]
        string_count[node] = spam[0][1] + spam[1][1]

    return [key for key in string_count][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


def decoding(string, codes):
    res = ''
    i = 0

    while i < len(string):

        for code in codes:

            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])

    return res


my_string = input('Введите строку для сжатия: ')
tree = get_tree(my_string)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(my_string, codes)
print('Сжатая строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)

if my_string == decoding_str:
    print('Успешно!')
else:
    print('Ошибка!')