# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.

# my_f = open('file.txt', 'r')
# content = my_f.readlines()
# print(content)
# my_f.close()

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
# my_file = open(r"my_f.txt", "w")  # raw
#
# if my_file.writable():
#     strings = ["Hello\n", "Natali\n", "Till\n"]
#     my_file.writelines(strings)
# else:
#     print("Can not write")
# my_file.close()
#
# with open("my_f.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line) - 1
#         print(f"{letters} letters in line")
#     print(f"String count is {lines}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из
# сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32
#
# person = {'Иванов': 17000, 'Петров': 21000, 'Сидоров': 45000, 'Щедров': 65000, 'Пельш': 70000, 'Яковенко': 41000, 'Шот': 55000, 'Кац': 65000, 'Енин': 19500, 'Носов': 5000}
# try:
#     file_obj = open("salary.txt", 'w')
#     for last_name, salary in person.items():
#         file_obj.write(last_name + ':' + str(salary) + "\n")
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_obj.close()
# summa = 0
# count = 0
# persons = []
# with open("salary.txt", "r") as file_obj:
#     for line in file_obj:
#         print(line, end="")
#         tokens = line.split(':')
#         if int(tokens[1]) <= 20000:
#             persons.append(tokens[0])
#         summa += int(tokens[1])
#         count += 1
# result = summa / count
# print(f"persons: {persons}")
# print(f"averate: {result}")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# file_obj = open("list.txt", "w")
#
# if file_obj.writable():
#     strings = ["One — 1\n", "Two — 2\n", "Three — 3\n", "Four — 4\n"]
#     file_obj.writelines(strings)
# else:
#     print("Can not write")
# file_obj.close()
# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_file = []
# with open('list.txt', 'r') as file_obj:
#     for i in file_obj:
#         i = i.split(' ', 1)
#         new_file.append(rus[i[0]] + '  ' + i[1])
#     print(new_file)
#
# with open('file_new.txt', 'w') as file_obj_1:
#     file_obj_1.writelines(new_file)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле
# и выводить ее на экран.


# def summary():
#     try:
#         with open('number.txt', 'w') as file_obj:
#             line = input('Введите цифры через пробел \n')
#             file_obj.writelines(line)
#             my_numb = line.split()
#
#             print(sum(map(int, my_numb)))
#     except IOError:
#         print('Ошибка в файле')
#     except ValueError:
#         print('Неправильно набран номер. Ошибка ввода-вывода')
# summary()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
# import re
#
# report = {}
# with open('subject.txt', 'r', encoding='UTF-8') as file:
#     text = file.read()
#     file.seek(0)
#     for row in file:
#         row_items = row.split(': ')
#         hours = re.findall(r"\d+", row_items[1])
#         report.update({row_items[0]: sum([int(i) for i in hours])})
#
# print(f"Исходный файл:\n{text}\n")
# print(f"Словарь:\n{report}")

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее
# не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также
# добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
#
# from json import dumps
#
# SRC_FILENAME = "firm.txt"
# DST_FILENAME = "prof.json"
#
# results = [{}, {}]
#
# try:
#     with open(SRC_FILENAME, 'r') as fhs:
#         lines = fhs.readlines()
#
#     for line in lines:
#         name, form, proceeds, expenses = line.split()
#         results[0][name] = int(proceeds) - int(expenses)
#
#     results[1]['average_profit'] = round(
#         sum(profit for form, profit in results[0].items() if profit / len(results[0])) > 0)
#
#     with open(DST_FILENAME, "w") as fhd:
#         fhd.write(dumps(results))
# except IOError as e:
#     print(e)
# except ValueError:
#     print("Неконсистентные данные")
