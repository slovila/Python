# Задача №1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



# with open('/Users/alekseynikitenko/Desktop/Python_lessons/Python/HomeWork_5/zadanie_1,1.txt', 'r', encoding='utf-8') as file:
#     text = file.read()

# text = text.split()

# for i in range(len(text)):
#     if 'абв' and ',' in text[i]:
#         text[i] = ','
#     elif 'абв' and '.' in text[i]:
#         text[i] = '.'
#     elif 'абв' in text[i]:
#         text[i] = ''

# text = ' '.join( text)
# text = text.replace('  ', ' ')
# text = text.replace(' ,', ',')
# text = text.replace(' .', '.')
# with open('/Users/alekseynikitenko/Desktop/Python_lessons/Python/HomeWork_5/zadanie_1,2.txt', 'w', encoding='utf-8') as file:
#     file.write(text)
    
    
    
    
# Задача №2 Создайте программу для игры с конфетами человек против человека.
# 
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 
# a) Добавьте игру против бота
# 
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint
# from secrets import choice


# def Player(player_number, candys):
#     print('Игрок ',player_number)
#     while True:
#         hod = int(input('Введите количество конфет от 1 до 28 -> '))
#         if 0 < hod < 29:
#             candys -= hod
#             print(candys)
#             break
#         else:
#             print('Неправильный ввод')
#     return candys

# def Com_Player(candys):
#     print('Компьютер')
#     grab = candys % 29
#     if grab == 0:
#         grab = randint(1,28)
#     print('Взял -> ', grab)
#     candys -= grab
#     print(candys)

#     return candys

# def Game(player_coll = 1, candys = 2021):
#     player_1 = choice([True, False])

#     while candys > 28:
#         if player_1:
#             candys = Player(1, candys)
#             player_1 = not player_1
#         elif player_coll == 2:
#             candys = Player(2,candys)
#             player_1 = not player_1
#         else:
#             candys = Com_Player(candys)
#             player_1 = not player_1

#     if player_1:
#         print('Игрок 1 победил')
#     elif player_coll == 2:
#         print('Игрок 2 победил')
#     else:
#         print('Компьютер победил')

# coll = int(input('Введите количество игроков(1 или 2) -> '))
# Game(coll, 2021)


# Задача №3 Создайте программу для игры в ""Крестики-нолики"".

# def Game(table):
#     player_1 = True
#     win = False

#     for number in range(9):
#         if player_1:
#             print('Игрок X')
#         else:
#             print('Игрок O')
#         hod = input('Введите номер-> ')
#         for i in range(len(table)):
#             for j in range(len(table[i])):
#                 if table[i][j] == hod:
#                     if player_1:
#                         table[i][j] = 'X'
#                     else:
#                         table[i][j] = 'O'           
#         for i in table:
#             print(i)

#         if number > 4:
#             win = Check(table)
#             if win:
#                 if player_1:
#                     print('X Победил')
#                     break
#                 else:
#                     print('O Победил')
#                     break
#         player_1 = not player_1
        
#     if not win:
#         print('Ничья')

# def Check(table):
#     win = False
#     if table[0][0] == table[0][1] == table[0][2]:
#         win = True
#     elif table[1][0] == table[1][1] == table[1][2]:
#         win = True
#     elif table[2][0] == table[2][1] == table[2][2]:
#         win = True
#     elif table[0][0] == table[1][0] == table[2][0]:
#         win = True
#     elif table[0][1] == table[1][1] == table[2][1]:
#         win = True
#     elif table[0][2] == table[1][2] == table[2][2]:
#         win = True
#     elif table[0][0] == table[1][1] == table[2][2]:
#         win = True
#     elif table[2][0] == table[1][1] == table[0][2]:
#         win = True
#     return win


# table = [['1','2','3'],['4','5','6'],['7','8','9']]
# for i in table:
#     print(i)
# Game(table)


# Задача №4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def First_Iteration_Pack(text1):
    text2 = ''
    mem = text1[0]
    count = 1
    i = 1
    while i < len(text1):
        if mem[0] == text1[i]:
            count += 1
            i += 1
        elif mem[0] != text1[i]:
            text2 = text2 + str(count) + mem[0]
            mem = text1[i]
            count = 1
            i += 1
            if i == len(text1):
                text2 = text2 + str(count) + mem[0]

    return text2

def Second_Iterarion_Pack(text1):
    text2 = ''
    first = -1
    last = -1
    i = 0
    while i < len(text1):
        if first == -1 and text1[i] != '1':
            text2 = text2 + text1[i]
            i += 1
        elif text1[i] == '1' and first == -1:
            first = i
            i += 1
        elif (first != -1 and text1[i].isdigit() and text1[i] != '1') or (i == (len(text1) - 1) and first != -1):
            last = i
            if i != len(text1) - 1:
                mem = text1[first:last]
            else:
                mem = text1[first:]
            mem = mem.replace('1','')
            text2 = text2 + '-' + str(len(mem)) + mem
            first = -1
            last = -1
            if i == len(text1) - 1:
                break
        else:    
            i +=1        
    return text2

def Repack(text1):
    text2 = ''
    i = 0
    coll = ''
    long = 0
    while i < len(text1):
        if text1[i] == '-':
            long = ''
            i += 1
        elif long != 0 and text1[i].isdigit():
            long += text1[i]
            i += 1
        elif long != 0 and not text1[i].isdigit():
            long = int(long)
            text2 += text1[i]
            i += 1
            long -= 1
        elif text1[i].isdigit() and long == 0:
            coll += text1[i]
            i += 1
        elif coll != '' and not text1[i].isdigit():
            text2 += Repack1(text1[i],int(coll))
            coll = ''
            i += 1
    return text2

def Repack1(text1,coll):
    text2 = ''
    for i in range(coll):
        text2 += text1
    return text2

with open('/Users/alekseynikitenko/Desktop/Python_lessons/Python/HomeWork_5/zadanie_4,1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

text1 = First_Iteration_Pack(text1)
text1 = Second_Iterarion_Pack(text1)

with open('/Users/alekseynikitenko/Desktop/Python_lessons/Python/HomeWork_5/zadanie_4,2.txt', 'w', encoding='utf-8') as file:
    file.write(text1)

with open('/Users/alekseynikitenko/Desktop/Python_lessons/Python/HomeWork_5/zadanie_4,2.txt', 'r', encoding='utf-8') as file:
    text1 = file.read()

text1 = Repack(text1)

with open('/Users/alekseynikitenko/Desktop/Python_lessons/Python/HomeWork_5/zadanie_4,3.txt', 'w', encoding='utf-8') as file:
    file.write(text1)
