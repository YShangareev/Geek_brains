'''Task 1'''


def division(a, b):
    try:
        div_1 = a / b
        div_2 = b / a
    except ZeroDivisionError:
        if a == 0:
            print(f'a/b: {0}')
            print('b/a: Деление на 0 невозможно')
        elif b == 0:
            print('a/b: Деление на 0 невозможно')
            print(f'b/a: {0}')

            '''Подскажите почему возникает ошибка при выполнении кода ниже, вроде назначение переменной раньше есть'''
            # print(f'b/a: {div_2}')

    else:
        print(f'a/b: {div_1}\nb/a: {div_2}')


first_number = float(input('Введите число a:'))
second_number = float(input('Введите число b:'))

division(first_number, second_number)

'''Task 2'''


def information_by_people(name=None, second_name=None, years_of_birth=None, living_city=None, email=None, phone=None):
    print(
        f'Имя:{name} Фамилия:{second_name} Год рождения:{years_of_birth} Город проживания:{living_city} Email:{email} Телефон:{phone}')


information_by_people(name='Yan', second_name='Shangareev', years_of_birth='1997', living_city='Ufa')
'''Task 3'''
import heapq


def sum_largest_number_by_heapq(a, b, c):
    my_list = [a, b, c]
    two_largest_number = heapq.nlargest(2, my_list)
    largest_of_sum = sum(two_largest_number)
    print(f'Сумма:{largest_of_sum}')


def sum_largest_number(a, b, c):
    my_list = [a, b, c]
    max_first = max(my_list)
    min_number = min(my_list)
    max_second = 0
    for i in my_list:
        if min_number < i < max_first:
            max_second = i
    largest_sum = max_first + max_second
    print(largest_sum)


a = float(input('Введите число a:'))
b = float(input('Введите число b:'))
c = float(input('Введите число c:'))

sum_largest_number_by_heapq(a, b, c)
sum_largest_number(a, b, c)

'''Task 4'''


def exponentiation(x, y):
    return x ** y


def exponentiation_cycle(x, y):
    count = 0
    sqr = 1
    while count != abs(y):
        sqr /= x
        count += 1
    return sqr


x = int(input('Введите число x(положительное целое):'))
y = int(input('Введите число y(отрицательное целое):'))

print(exponentiation(x, y))
print(exponentiation_cycle(x, y))

'''Task 5'''


def sum_of_number():
    running = True
    sum_number = 0
    while running:
        string = input('Введите числа через пробел:')
        string_list = string.split()
        if string_list[0] == 'выход':
            running = False
        elif string_list[-1] == 'выход':
            string_list_number = [int(i) for i in string_list[:-1]]
            sum_numbers = sum(string_list_number)
            sum_number += sum_numbers
            print(sum_number)
            running = False
        else:
            string_list_number = [int(i) for i in string_list]
            sum_numbers = sum(string_list_number)
            sum_number += sum_numbers
            print(sum_number)


sum_of_number()

'''Task 6,7'''


def text_format(word=None, string=None):
    word_first_symbol_large = word.capitalize()
    string_first_symbol_all_words_large = string.title()
    print(f'Слово:{word_first_symbol_large}\nСтрока:{string_first_symbol_all_words_large}')


word = input('Введите слово:')
string = input('Введите строку:')
text_format(word=word, string=string)