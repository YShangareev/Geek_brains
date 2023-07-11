from sys import argv

'''Task 1'''

'''salary = (rate per hour * hour) + bonus'''
script_name, rate_per_hour, hours, bonus = argv

print('Часовая ставка:', rate_per_hour)
print('Отработано часов:', hours)
print('Премия:', bonus)

salary = float(rate_per_hour) * float(hours) + float(bonus)
print('Зарплата:', salary)


'''Task 2'''

import random


my_list = [random.randint(-100, 100) for i in range(20)]

print(my_list)

my_list_2 = []
count = 0

for i in range(len(my_list)-1):
    if my_list[i] < my_list[i + 1]:
        my_list_2.append(my_list[i + 1])

print(my_list_2)

'''Task 3'''

my_list_number = [i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0]
print(my_list_number)


'''Task 4'''

my_list_numbers = [random.choice(range(0, 50)) for i in range(20)]
print(my_list_numbers)

my_list_numbers_string = ' '.join(map(str, my_list_numbers))

unique_numbers = []

for i in my_list_numbers:
    if my_list_numbers_string.count(str(i)) == 1:
        unique_numbers.append(i)

print(unique_numbers)

from functools import reduce

'''Task 5'''

my_list_task_5_numbers = [i for i in range(100, 1001) if i % 2 == 0]

result = reduce(lambda x, y: x * y, my_list_task_5_numbers)

print(result)

import itertools

'''Task 6'''

while True:
    my_list_lask_6 = [i for i in itertools.count(5)]
    if len(my_list_lask_6) >= 20:
        break

my_list_string_task_6 = ['I', 'L', 'Y']

count = 0

for i in itertools.cycle(my_list_string_task_6):
    print(i)
    count += 1
    if count == 10:
        break


'''Task 7'''


def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

for i in fact(5):
    print(i)
