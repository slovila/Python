'''Задание 1:
#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
#  желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#  третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
#  порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time

class TrafficLight():

    # Определяем время ожидания сигнала светофора
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 4

    # Определяем названия цветов сигналов светофора
    red_color_name = 'красный'
    yellow_color_name = 'желтый'
    green_color_name = 'зеленый'

    def __init__(self, color):
        self.__color = color
        print(f'\nСоздан новый объект TrafficLight со стартовым цветом {self.__color}')

    def switch_light(self, color, wait_period):
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color = ''):

        # Если при вызове метода цвет не указан, берем из родительского класса
        # В противном случае стартуем с цвета, объявленного при вызове метода
        if not color:
            loc_color = self.__color
        else:
            loc_color = color

        if loc_color == self.red_color_name:
            self.switch_light('красный', self.red_color_wait)
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        elif loc_color == self.yellow_color_name:
            self.switch_light('желтый', self.yellow_color_wait)
            self.switch_light('зеленый', self.green_color_wait)
        else:
            self.switch_light('зеленый', self.green_color_wait)

        print('Цикл переключения цветов завершен')

tl1 = TrafficLight('красный')
tl1.running()

tl2 = TrafficLight('желтый')
tl2.running()

tl3 = TrafficLight('зеленый')
tl3.running()

# Инициализируем класс красным цветом, а метод запускаем с желтого
tl1 = TrafficLight('красный')
tl1.running('желтый')'''


# Задание 2:
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():

    # Вес асфальта в тоннах для 1 кв.м. полотна толщиной в 1 см
    # Определяю его как private из соображений, что это константа, не подлежащая изменению
    __weight = 0.5

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Создан новый объект класса Road длиной {self._length} метров и шириной {self._width} метров')

    def get_weight(self, thickness):
        ret_val = self._length * self._width * thickness * self.__weight
        print(f'Вес асфальта, требуемый для укладки полотна толщиной {thickness} см, равен {ret_val} т')

        return ret_val

r1 = Road(100, 5)
w1 = r1.get_weight(10)

r2 = Road(1000, 20)
w2 = r2.get_weight(20)

print(f'Суммарный вес асфальта для двух объектов = {w1 + w2}')





