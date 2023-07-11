import datetime
from colorama import init, Fore

init(autoreset=True)


'''Task 1'''


class Date():

    def __init__(self, date):
        self.date = date

    @classmethod
    def data_number(cls, date):
        date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
        day = date.day
        month = date.month
        year = date.year
        return f'Наша дата:{date}\nЧисло:{day, type(int(day))}\nМесяц:{month, type(int(month))}\nГод:{year, type(int(year))}'

    @staticmethod
    def validation(date):
        try:
            date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
        except ValueError:
            print(Fore.LIGHTRED_EX + f'Invalid_date_format(d-m-Y): {date} ')


print(Date.data_number('28-01-2022'))
Date.validation('31-02-2022')

'''Task 2'''

class division_by_zero(ZeroDivisionError):
    def __init__(self, zero):
        ZeroDivisionError.__init__(self)
        self.zero = zero


try:
    a = int(input('Please input number(1):'))
    b = int(input('Please input number(1):'))
    if int(b) == 0:
        raise division_by_zero(0)
    else:
        res = a / b
except division_by_zero as ex:
    print(f'res = {ex.zero}')


'''Task 3'''

class Isdigit(Exception):
    def __init__(self):
        Exception.__init__(self)

my_list = []
while True:
    some_text = input('Please input some text without whitespace:')
    if some_text == 'exit':
        break
    else:
        try:
            if not some_text.isdigit():
                raise Isdigit
        except Isdigit:
            print("Input doesn't integer")
            continue
        else:
            my_list.append(some_text)

print(my_list)


'''Task 4,5,6'''
class String_down(Exception):
    def __init__(self):
        Exception.__init__(self)

class Most_big_data(Exception):
    def __init__(self):
        Exception.__init__(self)

class Office_equipment:
    part_number = None
    division_name = None

    def __init__(self, quantity_of_certain_type, total_number):
        self.quantity_of_certain_type = quantity_of_certain_type
        self.total_number = total_number
        try:
            if isinstance(self.quantity_of_certain_type, str) == True or isinstance(self.total_number, str) == True:
                raise String_down()
            if int(self.quantity_of_certain_type) > int(total_number):
                raise Most_big_data()
        except String_down:
            print(Fore.LIGHTRED_EX + 'Неверный формат(quantity_of_certain_type) или (total_number)\nДолжен быть:(integer)')
        except Most_big_data:
            print(Fore.LIGHTYELLOW_EX + '(quantity_of_certain_type) не может быть больше (total_number)')


class Printer(Office_equipment):
    amount_of_paper_consumed = None


class Storehouse:
    def __init__(self, number_of_divisions):
        try:
            self.number_of_divisions = number_of_divisions
            if isinstance(self.number_of_divisions, str) == True:
                raise String_down()
        except String_down:
            print(Fore.LIGHTRED_EX + f'Неверный формат (number_of_divisions)\nДолжен быть:(integer)')

    def add(self, equipment_part_number, equipment_division):
        storehouse = {}
        storehouse[equipment_division] = equipment_part_number
        print(storehouse)


store = Storehouse(number_of_divisions=5)

oe = Office_equipment(quantity_of_certain_type=10, total_number=50)

printer = Printer(quantity_of_certain_type=None, total_number=None)
printer.part_number = 'sdfgfh487645'
printer.division_name = 'management'

store.add(printer.division_name, printer.part_number)

'''Task 7'''

class complex_number:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2


    def __add__(self, other):
        a = complex(self.number_1,self.number_2)
        y = complex(other.number_1, other.number_2)
        res = a + y
        return res

    def __mul__(self, other):
        a = complex(self.number_1, self.number_2)
        y = complex(other.number_1, other.number_2)
        res = a * y
        return res

a = complex_number(1,2)
b = complex_number(3,4)

print(a+b)
print(a*b)