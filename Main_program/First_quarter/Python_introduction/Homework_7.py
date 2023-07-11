'''Task 1'''

class Matrix():

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        a = len(self.matrix)
        b = len(other.matrix[0])
        for i in range(a):
            for j in range(b):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                res = self.matrix
        return Matrix(res)

    def __str__(self):
        qwe = [str(i) for i in self.matrix]
        a = (str([''.join(str(str(j).strip('[]')).split(',')) for j in qwe]).strip('[]')).replace("'", '')
        start = 0
        end = a.find(',')
        string = ''
        count = 0
        while count != len(qwe):
            c = a[start:end] + '\n'
            string += c.strip(' ')
            start = end + 1
            end += end + 2
            count += 1
        return string


mx = Matrix([[1, 2, 3], [2, 5, 6], [5, 8, 9]])
mx_2 = Matrix([[9, 8, 7], [8, 5, 4], [5, 2, 1]])
print(mx)
print(mx_2)
print(mx + mx_2)


'''Task 2'''

from abc import abstractmethod


class clothes():

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self):
        pass


class coat(clothes):
    def __init__(self, V):
        self.V = V

    def calculate(self):
        res = int(self.V) / 6.5 + 0.5
        return res


class smoking(clothes):
    def __init__(self, H):
        self.H = H

    def calculate(self):
        res = int(self.H) * 2 + 0.3
        return res


coat = coat(50)
print(f"Расход ткани на пальто: {round(coat.calculate(), 2)} м.")
smoking = smoking(180)
print((f"Расход ткани на пальто: {round(smoking.calculate() / 100, 2)} м."))
print(f"Общий расход ткани: {round(coat.calculate() + smoking.calculate() / 100, 2)} м.")

'''Task 2(@property decorator)'''

class User():
    user_count = 0

    def __init__(self, name, login, password):
        User.user_count += 1
        self.name = name
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    try:
        @password.setter
        def password(self, value):
            if len(value) >= 5:
                self.__password = value
            else:
                print('Invalid password length(mast be lenght >= 5 symbol')
    except NameError:
        pass

    def show_info(self):
        return f'User name - {self.name}, User Login - {self.__login}'

class SuperUser(User):
    admin_count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        SuperUser.admin_count += 1

    def show_info(self):
        return f'User login - {self.__login}, User role - {self.__role}'

user1 = User(name='Alexey', login='ASmirnov', password='12345')
user2 = User(name='Andrey', login='AAlekseev', password='67890')
user3 = User(name='Ivan', login='IFedorov', password='qwerty')
admin = SuperUser(name='Liana', login='LKarimova', password='secure', role='admin')
users = User.user_count
admins = SuperUser.admin_count
print(f'Всего пользователей - {users}')
print(f'Всего администраторов - {admins}')

'''Task 3'''


class cell():
    def __init__(self, number_of_cell_of_the_cell):
        self.number_of_cell_of_the_cell = number_of_cell_of_the_cell

    def __add__(self, other):
        a = int(self.number_of_cell_of_the_cell)
        b = int(other.number_of_cell_of_the_cell)
        res = a + b
        return res

    def __sub__(self, other):
        a = int(self.number_of_cell_of_the_cell)
        b = int(other.number_of_cell_of_the_cell)
        if a - b >= 0:
            res = a - b
        else:
            return 'Разность количества клеток < 0, операция невозможна'
        return res

    def __mul__(self, other):
        a = int(self.number_of_cell_of_the_cell)
        b = int(other.number_of_cell_of_the_cell)
        res = a * b
        return res

    def __truediv__(self, other):
        a = int(self.number_of_cell_of_the_cell)
        b = int(other.number_of_cell_of_the_cell)
        res = a // b
        return res

    def make_order(self, number_of_cell_of_the_row):
        my_list = [i for i in range(1, int(self.number_of_cell_of_the_cell))]
        a = str(my_list).strip('[]').split(',')
        start = 0
        string = ''
        count = 0
        end = number_of_cell_of_the_row
        stop = len(my_list) // number_of_cell_of_the_row + 1
        while count != stop:
            b = str(a[start:end])
            string += b.strip('[]').replace("', '", '').strip("'").strip(' ') + '\n'
            start += int(number_of_cell_of_the_row)
            end += int(number_of_cell_of_the_row)
            count += 1
        return string


cell_1 = cell(12)
cell_2 = cell(3)
print(f'Сложение клеток: {cell_1 + cell_2}')
print(f'Разность клеток: {cell_1 - cell_2}')
print(f'Умножение клеток: {cell_1 * cell_2}')
print(f'Деление клеток: {cell_1 / cell_2}')
print(cell_1.make_order(5))