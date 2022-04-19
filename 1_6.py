# Задание 1
import time
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зелёный']

    def running(self):
        for i in range(len(self.__color)):
            print("\033[31m {}" .format(self.__color[i]))
            time.sleep(7)
            print("\033[33m {}" .format(self.__color[i + 1]))
            time.sleep(2)
            print("\033[32m {}" .format(self.__color[i + 2]))
            time.sleep(5)
            return

Drive = TrafficLight()
Drive.running()

# Задание 2
class Road:
    def __init__(self, length,  width):
        self._l = length
        self._w = width

    def massa(self):
        self.m = self._l * self._w * 25 * 5
        return self.m

Rasschet = Road(50, 2000)           # Создала новый объект класса Road
print(f' Масса = {Rasschet.massa() / 1000} т.')     # использовала

# Задание 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {'zp': wage, 'bon': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.n} {self.s}'

    def get_total_income(self):
        return f'{sum(self._income.values())}'

sotr1 = Position('Иванов', 'Олег', 'кладовщик', 15000, 5000)
print(sotr1.get_full_name())
print(sotr1.get_total_income())

# Задание 4
class Car:
    def __init__(self, speed, color, name, is_polise = False):
        self.s = speed
        self.c = color
        self.n = name
        self.i = is_polise

    def go(self):
        return f'Машина {self.n} поехала'

    def stop(self):
        return f'Машина {self.n} остановилась'

    def turn(self, direction):
        self.d = direction
        if self.d == 1:
            a = 'налево'
        else:
            a = 'направо'
        return f'Машина {self.n} поехала {a}'

    def show_speed(self):
        return f'Скорость машины {self.n}: {self.s}'

class TownCwar(Car):
    def show_speed(self):
        if self.s > 60:
            t = 'с превышением превышением скорости'
            print(f'Машина {self.n} едет {t}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            w = 'с превышением превышением скорости'
        print(f'Машина {self.n} едет {w}')

class Police(Car):
    def __init__(self, speed, color, name, is_polise = True):
        Car.__init__(speed, color, name, is_polise)

town_car = TownCwar(70, 'Серый', 'Пежо')
print(town_car.go())
print(town_car.stop())
town_car.show_speed()
print(town_car.turn(0))

police_car = SportCar(80, 'Белый', 'Мерседес')
print(police_car.show_speed())


# Задание 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'Используется {self.title}')

class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'Используется {self.title}')

class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print(f'Используется {self.title}')

pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()




