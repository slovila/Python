# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11

# float_num = input('input float number: ')
# # print(type(float_num))
# sum = 0
# for i in float_num:
#     if i != '.':
#         sum += int(i)
# print(sum)


# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')



# 3. Задайте список из n чисел 
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input('Enter number: ')) 

# def sequence(n):

#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
# print(sequence(n))
# print(round(sum(sequence(n))))

# 4. Реализуйте алгоритм перемешивания списка.

list = ['Sad But True', 250, 3.14, 'Raining Blood ']
print(list) 
import random
random.shuffle(list)
print('->', list) 