import collections

print('Задание №1')
"""
Пользователь вводит данные о количестве предприятий, их наименования 
и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
Программа должна определить среднюю прибыль (за год для всех предприятий) 
и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования 
предприятий, чья прибыль ниже среднего.
"""
n = int(input('Введите количество предприятий: '))
companies = { }
# companies = collections.namedtuple('Company', ['profit_1', 'profit_2', 'profit_3', 'profit_4', 'sum_profit'])

s = 0
total_profit = 0

for i in range(n):
    company_name = input('Введите название ' + str(i+1) + '-й компании: ')
    pr_1 = int(input('Введите прибыль за 1-й квартал в руб: '))
    pr_2 = int(input('Введите прибыль за 2-й квартал в руб: '))
    pr_3 = int(input('Введите прибыль за 3-й квартал в руб: '))
    pr_4 = int(input('Введите прибыль за 4-й квартал в руб: \n'))
    summ = pr_1 + pr_2 + pr_3 + pr_4
    companies[company_name] = summ
    total_profit += summ

print(companies)

avrg_profit = total_profit / n
print(f'Средняя прибыль для всех компаний в руб: {avrg_profit}')

for i in companies:
    if companies[i] > avrg_profit:
        print(f'Средняя прибыль компании {i} выше среднего')
    else:
        print(f'Средняя прибыль компании {i} ниже среднего')




