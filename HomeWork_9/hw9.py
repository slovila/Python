#  Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

# def to_dict(lst):
    # return {element: element for element in lst}

# Проверка
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))



#Иван решил создать самый большой словарь в мире. 
#Для этого он придумал функцию biggest_dict(**kwargs), 
#которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, 
#состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# my_dict = {'first_one': 'we can do it'}


# def biggest_dict(**kwargs):
    # my_dict.update(**kwargs)


# biggest_dict(k1=22, k2=31, k3=11, k4=91)
# biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
# print(my_dict)


# Задача№3
from collections import Counter


def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))

# проверка
print(count_it('1111111111222'))
print(count_it('123456789012133288776655353535353441111'))
print(count_it('007767757744331166554444'))



