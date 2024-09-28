import random
class Human:
    def __init__(self, name, job=None, car=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 50
        self.eat_level = 100

    def eat(self):
        eat = random.randint(1, 10)
        if self.house.food - eat <= 0:
            no_food = True
            while no_food:
                print('Ми на нулі! Треба купити їжу')
                self.shopping()
                if self.house.food - eat >= 0:
                    no_food = False
        self.eat_level += eat
        if self.eat_level >= 200:
            self.eat_level = 200
        print(f'Я захавав {eat}%')
        print(f'Я ситий на {self.eat_level}%')
        self.house.food -= eat

    def chill(self):
        print(f'Я відпочиваю')
        self.house.pollution += 5
        self.money -= 5
        if self.house.pollution >= 100:
            print(f'Господи я маю прибрати тут забрудно аж {self.house.pollution}')
            self.clean()
            print(f'Тепер тут настільки чисто {self.house.pollution}')

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food += random.randint(5, 10)
        self.eat_level -= 3
        if self.car != None:
            if self.car.drive(random.randint(1, 10)*10):
                print(f'Я поїхав на роботу')
            else:
                print('Пішли пішки')
        else:
            print('Пішли пішки')

    def clean(self):
        self.eat_level -= 5
        print(f'Я прибираю')
        c = random.randint(0, 1)
        if c == 1:
            print(f'Я генерально прибираю')
            self.house.pollution = 0
        else:
            print(f'Я злегка прибираю')
            self.house.pollution -= 5

    def work(self):
        self.eat_level -= 5
        self.money += 1
        print(f'Я відправляюсь на роботу')
        if self.car != None:
            if self.car.drive(20):
                print(f'Я поїхав на роботу')
            else:
                print('Пішли пішки')
        else:
            print('Пішли пішки')

    def info(self):
        print(f'Грощі {self.money}')
        print(f'Я ситий на {self.eat_level}%')

        if self.car != None:
            print(f'Стан авто, пальне {self.car.full}, стан {self.car.state}')

        print(self.job)
        print(self.house)

    def is_alive(self):
        if self.money <= 0 or self.eat_level <= 0:
            return True
        else:
            return False

    def live(self, day):
        print(f"День {day} з життя {self.name}")
        print("====================================")
        live_choise = random.randint(1, 5)
        if live_choise == 1:
            self.work()
        elif live_choise == 2:
            self.clean()
        elif live_choise == 3:
            self.eat()
        elif live_choise == 4:
            self.chill()
            self.eat()
        elif live_choise == 5:
            self.shopping()
            random_eat_time = random.randint(1,2)
            if random_eat_time == 1:
                self.eat()
        if day % 7 == 0:
            self.money += 50
            if car != None:
                self.car.add_full(random.randint(2,5))




class Car:
    def __init__(self, model):
        self.model = model
        self.pasagers = []
        self.full = 100
        self.state = 100

    def add_full(self, fuel):
        if self.full + fuel > 100:
            self.full = 100
            print(f'{self.full + fuel - 100} решта, ми намагаєось залити більше ніж можна')
        else:
            self.full += fuel
            print(f'Бак заправленно на {fuel}')

    def drive(self, V):
        delta_fuel = V * 0.1
        if self.full < 0:
            print('Неможливо виїхати пустий бак')
            return False
        else:
            self.full -= delta_fuel
            self.state = V * 0.01
            print(f'Ми проїхали {V} км, використали літрів {delta_fuel} пального')
            return True
    def add_pasager(self, *peoples):
        for human in peoples:
            self.pasagers.append(human)

    def print_pasager(self):
        print(f'Avto {self.model}')
        if self.pasagers != []:
            for pasager in self.pasagers:
                print(pasager.name)
        else:
            print('None pasagers')

class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Професія "{self.name}", \nЗарплатння {self.salary}'

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0
    def __str__(self):
        return f'Запас їжі {self.food},\nЗабрудненість {self.pollution}'

car = None
human1 = Human('Vlada', Job('Поліцейський', 50), car=car)
buy_car_day = None
for day in range(366):
    if human1.is_alive() == True:
        print('ти помер')
        break
    if human1.money >= 1000:
        if car is None:
            car = Car('BMW')
            print('Я купив машину!')
            print(f'В мене було {human1.money} грошей')
            human1.money -= 1000
            print(f'Тепер в мене {human1.money} грошей')
            buy_car_day = day
            human1 = Human('Vlada', Job('Поліцейський', 1500), car=car)
    human1.live(day)



human1.info()
if car != None:
    print(f'Я купив машину на {buy_car_day} день')
#human1.work()
#human2 = Human('Liza')
#car = Car('AUDI')
#car.add_pasager(human1, human2)
#car.print_pasager()