import time
from colorama import init, Fore
import emoji

init(autoreset=True)


class Error(Exception):
    def __init__(self, string):
        Exception.__init__(self)
        self.string = string


class TrafficLight():
    __color = ['Red', 'Orange', 'Green']

    def running(self):
        try:
            elements = self.__color
            if elements[0] != 'Red':
                raise Error('Red')
        except Error as ex_1:
            print(f'Error: wrong order. First element must be {ex_1.string}')
        else:
            try:
                for i in self.__color:
                    if i == 'Red':
                        print(i)
                        time.sleep(7)
                    elif i == 'Orange':
                        print(i)
                        time.sleep(2)
                    elif i == 'Green':
                        print(i)
                        time.sleep(10)
                    else:
                        raise Error(['Red', 'Orange', 'Green'])
            except Error as ex_2:
                print(f'Error: wrong element. Must be {ex_2.string}')


t = TrafficLight()
t.running()

class Road():
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calculate(self):
        mass = float(input('Please input mass of asphalt per 1m2 with a thickness of 1 cm(kg):'))
        depth = float(input('Please input depth of road cover(cm):'))
        calc = self._lenght * self._width * mass * depth / 1000
        print(f"Total amount of asphalt - {'{0:,}'.format(calc).replace(',', ' ')} t.")


a = Road(5000, 50)
a.calculate()


class Woker():
    name = None
    surname = None
    position = None
    _income = {
        'position': ['Head of planning Department', 'Specialist of the planning department', 'Deputy Chief Director'],
        'name': ['Fedorov Vladislav', 'Egorova Elizaveta', 'Korneva Anna'],
        'wage': [50000, 35000, 60000],
        'bonus': [0.5, 0.4, 0.66]
    }

    def __init__(self, position):
        self.position = position

    def get_full_name(self):
        full_name = f'{self.surname} {self.name}'
        return full_name

    def get_total_income(self):
        for i in self._income['name']:
            for j in self._income['position']:
                if self.get_full_name() == i and self.position == j:
                    a = self._income['name'].index(i)
                    total_income = float(self._income['wage'][a]) + float(self._income['wage'][a]) * float(
                        self._income['bonus'][a])
                    return total_income
                else:
                    print("Full name or position don't correspond to reality")


position = Woker('Head of planning Department')
position.name = 'Vladislav'
position.surname = 'Fedorov'
print(Fore.LIGHTBLUE_EX + f"Full name of workers: {position.get_full_name()}")
print(Fore.LIGHTYELLOW_EX + f"Position of workers: {position.position}")
print(Fore.LIGHTGREEN_EX + f"Total income of worker: {'{0:,}'.format(position.get_total_income()).replace(',', ' ')} RUB")


class Car():
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self, go):
        print(f"Let's go? {go}")
        time.sleep(2)

    def stop(self, stop):
        print(f'Stopped? {stop}')

    def direction(self, dir):
        print(f'Direction: {dir}')
        time.sleep(5)

    def show_speed(self):
        print(f'Current speed: {self.speed}')

    def show_name(self):
        print(f'Name car: {self.name}')


class TownCar(Car):
    def __init__(self, speed, color, name, car_body_type, speed_limit):
        super().__init__(speed, color, name)
        self.car_body_type = car_body_type
        self.speed_limit = speed_limit

    def speeding(self):
        if self.speed >= self.speed_limit:
            print(Fore.LIGHTRED_EX + 'Speed limit exceeded, slow down!')


class SportCar(Car):
    def __init__(self, speed, color, name, max_speed):
        super().__init__(speed, color, name)
        self.max_speed = max_speed


class WorkCar(Car):
    def __init__(self, speed, color, name, speed_limit):
        super().__init__(speed, color, name)
        self.speed_limit = speed_limit

    def speeding(self):
        if self.speed > self.speed_limit:
            print(Fore.LIGHTRED_EX + 'Speed limit exceeded, slow down!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = is_police


Car_1 = Car(speed=60, color='white', name='Hyundai')
Car_1.go('Yes')
Car_1.show_speed()
Car_1.direction('Go straight')
Car_1.speed = 50
Car_1.show_speed()
Car_1.direction('Left')
Car_1.stop('Yes')

TC = TownCar(speed=60, color='white', name='Hyundai', speed_limit=40, car_body_type='Hatchback')
TC.go('Yes')
TC.show_speed()
TC.speeding()
TC.speed = 39
TC.direction('Left')
TC.show_speed()
TC.speeding()
TC.direction('Right')
TC.stop('Yes')


class Stationery():

    def __init__(self, name):
        self.name = name

    def draw(self):
        print('Rendering ' + self.name)


class Pen(Stationery):
    def draw(self):
        if self.name == 'Pen':
            super().draw()
            print(emoji.emojize(":pen:"))
        else:
            print(Fore.LIGHTRED_EX+'Error')

class Pencil(Stationery):
    def draw(self):
        if self.name == 'Pencil':
            super().draw()
            print(emoji.emojize(":pencil:"))
        else:
            print(Fore.LIGHTRED_EX+'Error')


class Marker(Stationery):
    def draw(self):
        if self.name == 'Marker':
            super().draw()
            print("Unfortunately, I can't draw a marker, but I can draw a PENGUIN!!!!")
            print(emoji.emojize(":penguin:"))
        else:
            print(Fore.LIGHTRED_EX+'Error')

first = Pen('Pen')
first.draw()
second = Pencil('Pencil')
second.draw()
third = Marker('Marker')
third.draw()
fourth = Pen('1')
fourth.draw()
fifth = Pencil('2')
fifth.draw()
sixth = Marker('3')
sixth.draw()
