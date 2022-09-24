# # Задание. Дана последовательность чисел. 
# # Получить список уникальных элементов заданной последовательности.

# import List_generation as lg
# numbers_list = lg.list_generation()
# result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
# print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')


# # Задание. Найти сумму чисел списка стоящих на нечетной позиции

# import List_generation as lg
# numbers_list = lg.list_generation()
# sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
# odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
# print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')


# Задание. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

f = '3*x+1'
n = int(input('Количество элементов словаря: '))
d = {x: eval(f) for x in range(1, n+1)}
print(f'для {n = }: {d}')