#  1. Вычислить число c заданной точностью d. 
#     Пример: при d = 0.001, пи = 3.141. 10^-1 <= d >= 10^-10')

# def specified_accuracy(real_numb):
#     d = '0.000'
#     d = int(len(d) - 2)
#     accuracy_number = round(real_numb, d)
#     return accuracy_number

# n = float(input('Введите любое вещественное число: '))
# t = specified_accuracy(n)
# print(t)


# 2: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# original_number = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {original_number} приведены в списке: {lst}")


# 3. Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

# import random
# list = [random.randint(0,15) for i in range (20)]
# print(list)
# new_list =[]
# [new_list.append(i) for i in list if i not in new_list ]
# print(new_list)

# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools as it


# def ratios_list(k):
#     ratios = [randint(0, 10) for i in range(k + 1)]
#     if ratios[0] == 0:
#         ratios[0] = randint(1, 10)
#     return ratios


# def polynom_list(cof, ratios):
#     op = ['*x^']*(cof-1) + ['*x']
#     polynom = [[a, b, c] for a, b, c in it.zip_longest(
#         ratios, op, range(cof, 1, -1), fillvalue='') if a != 0]
#     for x in polynom:
#         x.append(' + ')
#     polynom = list(it.chain(*polynom))
#     polynom[-1] = ' = 0'
#     return "".join(map(str, polynom)).replace(' 1*x', ' x')


# cof = randint(2, 5)
# ratios = ratios_list(cof)
# polynom = polynom_list(cof, ratios)
# print(polynom)

# with open('Polynom_1.txt', 'w') as data:
#     data.write(polynom)

