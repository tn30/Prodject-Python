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