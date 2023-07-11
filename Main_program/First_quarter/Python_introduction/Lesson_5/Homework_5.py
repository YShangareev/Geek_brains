import json

"""Task 1"""

with open('lesson_5.txt', 'w', encoding='utf-8') as f:
    while True:
        user_string_1 = input('Введите что-нибудь: ')
        f.write(user_string_1 + '\n')
        if user_string_1 == '':
            break

"""Task 2"""

with open('Lesson_5_Task_2.txt', 'r', encoding='utf-8') as f:
    string_2 = f.readlines()
    print(string_2)
    print(len(string_2))
    for i in string_2:
        print(f'Строка с индексом {string_2.index(i)} имеет количество слов:' + str(len(i.split())))

"""Task 3"""

with open('salary.txt', 'r', encoding='utf-8') as f:
    string_3 = f.readlines()
    print(string_3)
    salary_of_workers = []
    for i in string_3:
        if int(i.split()[1]) < 20000:
            print(i.split()[0])
        salary_of_workers.append(int(i.split()[1]))
    print(sum(salary_of_workers) / len(string_3))

"""Task 4"""

with open('numbers.txt', 'r', encoding='utf-8') as f:
    string_4 = f.readlines()

with open('numbers_rus.txt', 'w', encoding='utf-8') as f:
    strings_rus = []
    for i in string_4:
        i = i.split()
        if int(i[2]) == 1:
            i[0] = 'Один'
        elif int(i[2]) == 2:
            i[0] = 'Два'
        elif int(i[2]) == 3:
            i[0] = 'Три'
        elif int(i[2]) == 4:
            i[0] = 'Четыре'
        elif int(i[2]) == 5:
            i[0] = 'Пять'
        elif int(i[2]) == 6:
            i[0] = 'Шесть'
        elif int(i[2]) == 7:
            i[0] = 'Семь'
        elif int(i[2]) == 8:
            i[0] = 'Восемь'
        elif int(i[2]) == 9:
            i[0] = 'Девять'
        strings_rus.append(' '.join(i) + '\n')
    f.writelines(strings_rus)

"""Task 5"""

with open('sum_numbers.txt', 'w+', encoding='utf-8') as f:
    while True:
        user_string_5 = input('Введите числа через пробел: ')
        f.write(user_string_5)
        if user_string_5 == '':
            break
    f.seek(0)
    numbers_5 = f.readlines()
    sum_numbers = []
    for i in numbers_5:
        for a in i.split():
            sum_numbers.append(int(a))
    print(f'Сумма всех чисел в строке:{sum(sum_numbers)}')

"""Task 6"""

with open('study.txt', 'r', encoding='utf-8') as f:
    study = f.readlines()
    print(study)
    dict = {}
    for i in study:
        my_list = []
        for a in i.split()[1:]:
            a = a.replace('(пр)', '')
            a = a.replace('(л)', '')
            a = a.replace('(лаб)', '')
            a = a.replace(',', '')
            a = float(a)
            my_list.append(a)
            sum_study = sum(my_list)

        dict[i.split()[0]] = sum_study

print(dict)

"""Task 7"""

with open('profit_firm.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    dict = {}
    average_profit = {}
    profit = []
    for i in data:
        profit_list = []
        for a in i.split()[2:]:
            profit_list.append(float(a))
        dict[i.split(':')[0]] = profit_list[0] - profit_list[1]
    print(dict)
    for i in dict.values():
        if i > 0:
            profit.append(i)

    average_profit['average_profit'] = sum(profit) / len(profit)

my_list_task_6 = [dict, average_profit]
print(my_list_task_6)

with open('profit_and_average_profit.json', 'w') as f:
    json.dump(my_list_task_6, f, ensure_ascii=False)
