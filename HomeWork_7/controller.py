import os.path

import glv
from input_data import *
from output_data import *
from logger import *
from data_keeper import *
from oper import *

write_log('program start, ')

if not os.path.isfile(glv.log_file): # проверка наличия файла логов (из glv)
    init_log() 
    write_log('init_log_file' + glv.s_symb + glv.log_file + glv.s_symb)
if not os.path.isfile(glv.book_file): # проверка наличия файла тлф.книги (из glv)
    init_book() 
    write_log('init_phone_book_file' + glv.s_symb + glv.book_file + glv.s_symb)

next_action = greetings() 
while next_action == '1':
    if number_of_lines(glv.book_file) == 0: # проверка на наличие записей в тлф.книге
        message_on_empty_book() 
        if continue_or_exit() == '1': 
            opers = get_key(glv.log_oper, 'add_contact') 
        else:
            break
    else:
        opers = operation_selection() 
    match opers:
        case 1: 
            log_op = glv.log_oper[opers] + glv.s_symb
            log_op = log_op + iput_all() + glv.s_symb
            write_log(log_op)
        case 2: 
            log_op = glv.log_oper[opers] + glv.s_symb
            log_op += input_select()
            write_log(log_op) 
        case 3: 
            log_op = glv.log_oper[opers] + glv.s_symb
            log_op += add_contact()
            write_log(log_op)             
        case 4: 
            log_op = glv.log_oper[opers] + glv.s_symb
            log_op += del_contact()
            write_log(log_op)                       
    next_action = continue_or_exit() 
farewell()   
write_log('program shutdown, ')