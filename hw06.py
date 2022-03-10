# 1. Создать класс TrafficLight(светофор) и определить у него один атрибут color(цвет) и метод running(запуск).Атрибут
# реализовать как приватный.В рамках метода реализовать переключение светофора в
# режимы: красный, желтый, зеленый.Продолжительность первого состояния (красный) составляет 7 секунд, второго(желтый) — 2
# секунды, третьего(зеленый) — на ваше усмотрение.Переключение между режимами должно осуществляться только в
# указанном порядке(красный, желтый, зеленый).Проверить работу примера, создав экземпляр и вызвав описанный
# метод. Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
# и завершать скрипт.

# from time import sleep
#
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1
#
# TrafficLight = TrafficLight()
# TrafficLight.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для
# покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной
# в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
#
# class Road:
#     __length = None
#     __width = None
#     weigth = None
#     tickness = None
#
#     def __init__(self, _length, _width):
#         self._length = _length
#         self._width = _width
#
#
# class MassCount(Road):
#     def __init__(self, _length, _width, weigth, tickness):
#         super().__init__(_length, _width)
#         self.weigth = weigth
#         self.tickness = tickness
#
#     def mass(self):
#         return self._length * self._width * self.weigth * self.tickness / 1000
#         print(f'Требуется {mass} т на дорожное покрытие')
#
#
# r = MassCount(20, 5000, 25, 0.05)
# print(r.mass())

# 3.Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
#
# class Position(Worker):
#
#     def __init__(self, name, surname, position, wage, bonus):
#         super().__init__(name, surname, position, wage, bonus)
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def get_total_income(self):
#         return self._income.get('wage') + self._income.get('bonus')
#         # return f'{sum(self._income.values())}'
#
# a = Position('Сергей', 'Иванов', 'руководитель отдела', 100000, 25000)
# print(a.get_full_name())
# print(a.position)
# print(a.get_total_income())

# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также
# покажите результат.

# class Car:
#     # atributes
#     def __init__(self, speed, color, name, is_police = True):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     # methods
#     def go(self):
#         return f'{self.name} is started'
#
#     def stop(self):
#         return f'{self.name} is stopped'
#
#     def turn_right(self):
#         return f'{self.name} is turned right'
#
#     def turn_left(self):
#         return f'{self.name} is turned left'
#
#     def show_speed(self):
#         return f'Текущая скорость {self.name}  {self.speed}'
#
# class TownCar(Car):
#     def __init__(self, speed, color, name, is_police = True):
#         super().__init__(speed, color, name, is_police = True)
#
#     def show_speed(self):
#         print(f'Текущая скорость городского автомобиля {self.name}  {self.speed}')
#
#         if self.speed > 60:
#             return f'Скорость {self.name} выше, чем разрешено для городского автомобиля'
#         else:
#             return f'Скорость {self.name} нормально для городской машины'
#
# class SportCar(Car):
#     def __init__(self, speed, color, name, is_police = True):
#         super().__init__(speed, color, name, is_police = True)
#
#
# class WorkCar(Car):
#     def __init__(self, speed, color, name, is_police = True):
#         super().__init__(speed, color, name, is_police = True)
#
#     def show_speed(self):
#         print(f'Текущая скорость рабочего автомобиля {self.name}  {self.speed}')
#
#         if self.speed > 40:
#             return f'Скорость {self.name} выше, чем разрешено для работы автомобиля'
#
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police = True):
#         super().__init__(speed, color, name, is_police = True)
#
#     def police(self):
#         if self.is_police:
#             return f'{self.name} из отдела полиции'
#         else:
#             return f'{self.name} не из полиции'
#
#
# audi = SportCar(120, 'черного цвета', 'Audi', False)
# outlander = TownCar(80, 'белого цвета', 'outlander', False)
# lada = WorkCar(30, 'красного цвета', 'Lada', True)
# ford = PoliceCar(60, 'синий',  'Ford', True)
# print(lada.turn_left())
# print(f'When {outlander.turn_right()}, then {audi.stop()}')
# print(f'{lada.go()} with speed exactly {lada.show_speed()}')
# print(f'{lada.name} is {lada.color}')
# print(audi.show_speed())
# print(outlander.show_speed())
# print(ford.police())
# print(ford.show_speed())

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). Метод
# выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.
#
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'

pen = Pen('Ручку')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
