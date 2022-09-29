from datetime import datetime as date
import glv

def init_log(): # создание файла логов при отсутствии
    with open(glv.log_file, 'w', encoding='utf-8') as logs:
        logs.write('')

def write_log(log_oper: str): # добавление даты и времени операции + запись лога
    global log_file
    operation_time = date.today().strftime('%d.%m.%Y %H:%M:%S')
    log_oper = operation_time + glv.s_symb + log_oper + '\n'
    with open(glv.log_file, 'a', encoding='utf-8') as logs:
        logs.write(log_oper)
