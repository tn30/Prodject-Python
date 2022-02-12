Prodject-Python
*/Задание 1.*/
new_list = [15, None, "John", 'False', True, 8.1]
print(type(new_list))

new_tuple = (15, None, "John", 'False', True, 8.1)
print(type(new_tuple))

my_int = 10
my_float = 5.8
my_str = "Hello!"
my_list = ['a', '0']
my_tuple = ('d', '9')
my_dict = {'city': 'Novosibirsk', 'country': 'Russia'}

big_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in big_list:
    print(f'{i} is {type(i)}')

*/Задание 2*/
my_list = input("Введите элементы списка: ").split()

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(my_list)

/*Задание 3*/
number = int(input("Введите порядковый номер месяца в году: "))
if number <= 12 and number >= 1:
    season_dict = {1: 'январь - зима',
                  2: 'февраль - зима',
                  3: 'март - весна',
                  4: 'апрель - весна',
                  5: 'май - весна',
                  6: 'июнь - лето',
                  7: 'июль - лето',
                  8: 'август - лето',
                  9: 'сентябрь - осень',
                  10: 'октябрь - осень',
                  11: 'ноябрь - осень',
                  12: 'декабрь - зима'}
    season_list = list(season_dict.values())
    for i, el in enumerate(season_list):
        if i == number-1:
            print(f"Время года через list для месяца {season_list[i]}")
            break
    print(f"Время года через dict для месяца {season_dict[number]}")
else:
    print("Ошибочно введен номер месяца года")

/*Задание 4*/
my_str = input("Введите пожалуйста строку из нескольких слов: ")
a = my_str.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")
    
    /*Задание5*/
    number = int(input("Ведите, пожалуйста, номер рейтинга: "))
numbers = [7, 5, 3, 3, 2]

numbers.append(number)
numbers.sort(reverse=-1)

print(numbers)

/*Задание 6*/
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода нажмите 'Q', для продолжения 'Enter', для аналитики 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Current analytics \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

    goods = []
    while input("Хотите добавить товар? Введите да/нет: ") == 'да':
        number = int(input("Введите номер товара "))
        features = {}
        while input("Хотите добавить параметры товара? Введите да/нет:") == 'да':
            feature_key = input("Введите код товара: ")
            feature_value = input("Введите наименование товара: ")
            features[feature_key] = feature_value
        goods.append(tuple([number, features]))
    print(goods)
    # goods = [(1, {'name': 'компьютер', 'цена': '20000'}), (2, {'name': 'принтер', 'цена': '6000'})]
    analitics = {}
    for good in goods:
        for feature_key, feature_value in good[1].items():
            if feature_key in analitics:
                analitics[feature_key].append(feature_value)
            else:
                analitics[feature_key] = [feature_value]
    print(analitics)
