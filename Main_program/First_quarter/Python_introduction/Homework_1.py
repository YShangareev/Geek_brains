import time

'''Задание 1'''

a = input('Введите число:')
b = input('Пожалуйста введите число:')
print(f'{a}\n{b}')


'''Задание 2'''

def time_sec_to_day_hour_minute(n):
    day = n // (24 * 3600)
    n -= day * 24 * 3600
    hour = n // 3600
    n -= hour * 3600
    minute = n // 60
    n -= minute * 60
    seconds = n % 60
    print(f'{day}:{hour}:{minute}:{seconds}')
    print(f'Дни:{day} Часы:{hour} Минуты:{minute} Секунды:{seconds}')

time_sec_to_day_hour_minute(99999)

print(time.strftime('%D:%H:%M:%S', time.gmtime(200000)))


'''Задание 3'''

c = input('Введите число:')
sum = int(c) + int(c * 2) + int(c * 3)
print(sum)


'''Задание 4'''

number = input('Введите число(количество цифр >= 2):')

i = 0

while i <= len(number):
    max_number = 0
    for n in number:
        if int(n) > max_number:
            max_number = int(n)
            i += 1

print(max_number)


'''Задание 5,6'''

income = float(input('Введите прибыль:'))
costs = float(input('Введите затраты на производство:'))
net_income_on_sales = income - costs
if net_income_on_sales < 0:
    print(f'Прибыль от продаж составила - ({abs(net_income_on_sales)}$)')
else:
    return_on_sales = (net_income_on_sales / income) * 100
    print(f'Прибыль составила - {net_income_on_sales}$')
    print(f'Рентабельность продаж:{round(return_on_sales, 2)}%')
    workforce = int(input('Введите численность сотрудников:'))
    profit_per_person = net_income_on_sales / workforce
    print(f'Прибыль на 1-го рабочего:{round(profit_per_person, 2)}$')


'''Задание 7'''

start_km = int(input('Введите начальное количество километров:'))
desired_km = int(input('Введите желаемов количество километров:'))

cont = 1
while start_km < desired_km:
    start_km = start_km + start_km * 0.1
    cont += 1

print(cont)