import pandas as pd
import glv

def string_format(phone_dict): # вывод таблицей - построчный (из словаря)
    print('\n')
    print(pd.DataFrame(phone_dict))

def column_format(phone_list): # вывод в столбец с разделением пустой строкой (из списка)
    print('\n')
    for i in range(len(phone_list)):
        for j in range(len(glv.title)):
            print(f'{glv.title[j]}: {phone_list[i][j]}')      
        print()