'''Task 1'''


def my_sckript(my_list):
    for i in my_list:
        print(f'Тип элемента {my_list.index(i)}: {type(i)}')


my_list_1 = [1, 'one', 2.1, False]

my_list_2 = [1, 'one', 2.1, True, False, True]

my_sckript(my_list_1)

my_sckript(my_list_2)

'''Task 2'''

my_list_3 = []
a = int(input('Введите количество элементов в списке:'))
while len(my_list_3) <= (a - 1):
    b = input('Введите элемент списка:')
    my_list_3.append(b)

print(my_list_3)

for i in range(len(my_list_3) // 2):
    my_list_3[2 * i], my_list_3[2 * i + 1] = my_list_3[2 * i + 1], my_list_3[2 * i]

print(my_list_3)

'''Task 3'''

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

while True:
    user_input = int(input('Введите номер месяца:'))
    if user_input in winter:
        print('Зима')
    elif user_input in spring:
        print('Весна')
    elif user_input in summer:
        print('Лето')
    elif user_input in autumn:
        print('Осень')
    else:
        print('Такого месяца не существует')
    if user_input == 0:
        break
seasons = {'Зима': [1, 2, 12],
           'Весна': [3, 4, 5],
           'Лето': [6, 7, 8],
           'Осень': [9, 10, 11]}

rev_season = dict((v, k) for k, val in seasons.items() for v in val)

while True:
    user_input_2 = int(input('Введите номер месяца:'))
    print(rev_season.get(user_input_2))
    if user_input_2 > 12:
        print('Такого месяца не существует')
    if user_input_2 == 0:
        break

'''Task 4'''

words_string = input('Введите несколько слов через пробел:')

for ind, word in enumerate(words_string.split(), 1):
    if len(word) > 10:
        print(f'{ind} {word[:10]}...')
    else:
        print(ind, word)

'''Task 5'''

my_rating_list = [9, 8, 7, 7, 5, 5]
number = int(input('Введите число рейтинга:'))
min_number = min(my_rating_list)
max_number = max(my_rating_list)
if number < min_number:
    my_rating_list.append(number)
elif number > max_number:
    my_rating_list.insert(0, number)
elif my_rating_list.count(number) > 1:
    pos = my_rating_list.index(number)
    my_rating_list.insert(pos + 1, number)

print(my_rating_list)

'''Task 6'''

products = []
analysis = {'Название': [],
            'Стоимость': [],
            'Количество': [],
            'Единица измерения': []}
while True:
    number_unit = input('Введите порядковый номер элемента:')
    if number_unit == 'Выход':
        break
    name_of_product = input('Введите название товара:')
    cost_product = int(input('Введите стоимость товара:'))
    counts_of_product = int(input('Введите количество единиц товара:'))
    unit_of_measurement = input('Введите единицу измерения количества товара:')
    one_product = {'Название': name_of_product,
                   'Стоимость': cost_product,
                   'Количество': counts_of_product,
                   'Единица измерения': unit_of_measurement}
    products.append((number_unit, one_product))
    analysis['Название'].append(name_of_product)
    analysis['Стоимость'].append(cost_product)
    analysis['Количество'].append(counts_of_product)
    analysis['Единица измерения'].append(unit_of_measurement)

print(products)
print(analysis)