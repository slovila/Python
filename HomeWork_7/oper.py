from ast import Return
from itertools import count
import glv
from logger import *
from input_data import *
from output_data import *
from data_keeper import *

def get_key(dict, value): # возврат ключа по содержимому значения словаря 
    for k, v in dict.items():
        if v == value:
            return k

def select_position_title(): # возврат номера позиции поиска в списке title
    select_list = ''
    for item in range(len(glv.sel_position)):
        select_list = select_list + str(glv.sel_position[item]) + '. ' 
        select_list = select_list + glv.title[item] +'\n'
    return select_sign(select_list)

def check_availability_data(num, value): # проверка наличия контактов по запросу
    list_name = name_to_list(num)
    count = 0
    for item in range(len(list_name)):    
        if value.lower() in list_name[item].lower() or value.lower() == list_name[item].lower():
            count += 1 
    return count

def print_input_select(contact_list): # вывод списка контактов
    choice = select_output_format()
    match choice:
        case 1:
            string_format(output_to_string(contact_list))
            log_f = glv.log_form[choice]
        case 2:
            column_format(contact_list)
            log_f = glv.log_form[choice]
    return log_f

def iput_all(): 
    return print_input_select(book_to_list())

def input_select():
    sel_pos = select_position_title() 
    log_s = glv.title[sel_pos] + glv.s_symb
    if sel_pos == 0:
        value = str(id_choice())
        log_s = log_s + value + glv.s_symb
        log_s = log_s + print_input_select(contact_to_list(0, value)) + glv.s_symb
    else:
        av_data = 0
        while av_data == 0:
            value = search_by_input(sel_pos)
            log_s = log_s + value + glv.s_symb
            av_data = check_availability_data(sel_pos, value)
            if av_data != 0:
                log_s = log_s + print_input_select(contact_to_list(sel_pos, value)) + glv.s_symb
            else:
                act = when_no_search_results()
                if act == 1:
                    av_data = 0
                elif act == 2:
                    name_to_list(sel_pos)
                    next_action = continue_or_exit()
                    if next_action == '1':
                        av_data = 0
                    else:
                        log_s += 'invalid value, the operation was interrupted by the user'
                        av_data = -1
                elif act == 3:
                    log_s += 'invalid value, the operation was interrupted by the user'
                    av_data = -1
    return log_s

def add_contact(): # ввод нового контакта -> только через терминал с диалогом
    return add_new_contact(input_contact())[:-2]

def del_contact():
    log_d = delete_contact(id_choice())
    contact_deletion_message()
    return log_d