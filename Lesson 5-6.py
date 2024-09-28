import random


class Human:
    def __init__(self, name, job=None, car=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def eat(self):
        eat = random.randint(1, 5)
        print(f"Я з'їв {eat}% їжи")
        self.house.food -= eat

    def chill(self):
        print(f"Я відпочиваю")
        self.house.pollution += 2
        self.money -= 5

    def shopping(self):
        self.money -= random.randint(1,10)
        if self.car != None:
            if self.car.drive(random.randint(1,10)*10):
                print("Поїхали в магазин")
        else:
            print("Сходили в магазин")
        self.house.food += random.randint(1,10)

    def cleaning(self):
        print("Я прибираю в будинку")
        c = random.randint(0, 1)
        if c == 1:
            print("Генеральне прибирання")
            self.house.pollution = 0
        else:
            print("Витерли пилюку")
            self.house.pollution -= 5
        if self.house.pollution < 0:
            self.house.pollution = 0

    def work(self):
        self.money += 30
        if self.car != None:
            if self.car.drive(20):
                print("Я поїхав на роботу")
            else:
                print("Я сходив на роботу")
        else:
            print("Я сходив на роботу")

    def info(self):
        print(f"Гроші - ${self.money}")
        if self.car != None:
            print(f"Стан автівки: пальне {self.car.fuel} л, стан {self.car.state}%")
        print(self.job)
        print(self.house)

    def is_alive(self):
        if self.money >= 0:
            return True
        else:
            return False

    def life(self, day):
        print()
        print(f"День {day} з життя {self.name}")
        print("====================================")
        self.work()
        self.chill()
        self.eat()
        self.shopping()

        if day % 7 == 0:
            self.cleaning()

        self.info()
        self.is_alive()



class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 100
        self.state = 100
        self.passengers = []

    def add_fuel(self, fuel):
        if self.fuel + fuel > 100:
            self.fuel = 100
            print(f"Ми намагаємся заправити більше ніж наш бак, решта {self.fuel + fuel - 100} літрів буде повернута грошима")
        else:
            self.fuel += fuel
            print(f"Авто заправлено на {fuel} літрів")

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel < 0:
            print("Подорож на авто не можлива, не вистачає пального")
            return False
        else:
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            print(f"Ми проїхали {length} км, використали {delta_fuel} л пального")
            return True

    def add_passenger(self, *peoples):
        for human in peoples:
            self.passengers.append(human)

    def print_passenger(self):
        print(f"Авто {self.model}:")
        if self.passengers != []:
            print("Зараз в авто їдуть:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print("Пасажирів немає")

class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Професія {self.name}, зарплатня ${self.salary}"


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Стан будинку: Холодильник забитий {self.food}%, забудненість {self.pollution}%"



human1 = Human("Serg", job=Job("Викладач", 1000))

for day in range(366):
    if human1.is_alive() == False:
        break
    human1.life(day)



# human2 = Human("Anna")
#
# car = Car("BMW X11")
# car.add_passenger(human1, human2)
#
# car.print_passenger()