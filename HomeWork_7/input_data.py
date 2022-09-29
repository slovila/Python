import glv
from data_keeper import *

def greetings(): # приветствие с переходом на диалог выбора дальнейшей работы или завершения
    print('Приветствую Вас в программе управления телефонной книгой!')
    return continue_or_exit()

def message_on_empty_book(): # сообщение при отсутствии записей в тлф.книге
    print('В настоящее время телефонная книга пуста. '
        'Вам доступна только операция добавления нового контакта.')

def contact_deletion_message(): # сообщение об удалении контакта
    print('Удаление выбранного контакта выполнено.')

def farewell(): # сообщение при завершении работы с программой
    print('Спасибо за пользование программой. До новых встреч!')

def continue_or_exit(): # диалог выбора дальнейшей работы или завершения
    return input('Для продолжения введите "1". \n'
                'Для завершения - любой другой символ: ')

def invalid_number(choice): # диалог о выборе действия при некорректном вводе (все диалоги)
    res_choice = 1
    if input(f'Вы ввели некорректное значение: {choice}.\n'
                'Если желаете продолжить, введите "1", '
                'в противном случае введите любой другой символ: ') != '1':
        res_choice = 0
    return res_choice

def choice_and_correct(options: list, message: str): # диалог выбора и проверки
                                                        #корректности ввода (все диалоги)
    choice = '-1'
    while not int(choice) in options:
        choice = input(message)
        if not int(choice) in options:
            if invalid_number(choice) == 0:
                choice = 0
                break
    return int(choice)

def input_contact(): # диалог ввода нового контакта через терминал
    print('Введите новый контакт.')
    contact = ''
    for item in range(1, len(glv.title)):
        user_text = ''
        while glv.s_symb in user_text or user_text == '':
            user_text = input(f'{glv.title[item]}: ')
            if glv.s_symb in user_text:
                print(f'Вы использовали системный символ "{glv.s_symb}". '
                        'Возможна некорректная работа программы.\n'
                        'Повторите ввод без системного символа.')
        contact = contact + user_text + glv.s_symb
    contact[:-2]
    return contact

def search_by_input(num): # диалог ввода символов для поиска контакта по позиции поиска
    return input(f'Введите несколько символов для поиска по позиции {glv.title[num]}: ')

def when_no_search_results(): # сообщение для диалога выбора 
                                # действий при отсутствии контактов по запросу
    print('Контакты, соответствующие Вашему запросу, отсутствуют.\n')
    message = 'Вам доступны следующие действия:\n' + glv.mess_actions
    message += 'Введите номер действия: '
    return choice_and_correct(glv.actions, message)

def operation_selection(): # сообщение для диалога выбора типа операции
    message = 'Вам доступны следующие операции:\n'+ glv.list_oper
    message += 'Введите номер операции: '
    return choice_and_correct(glv.operations, message)

def select_output_format(): # сообщение для диалога выбора формата вывода данных
    message = 'Вам доступны следующие форматы вывода:\n'+ glv.out_form
    message += 'Введите номер формата: '
    return choice_and_correct(glv.formats, message)

def select_sign(select_list): # сообщение для диалога выбора номера позиции поиска из title
    message = 'Поиск в телефонной книге воможен по следующим позициям:\n'+ select_list
    message += 'Введите номер позиции: '
    return choice_and_correct(glv.sel_position, message)

def id_choice(): # сообщение для диалога ввода id искомого контакта
    message = 'Введите id искомого контакта: '
    return choice_and_correct(id_to_list(), message)