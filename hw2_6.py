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

