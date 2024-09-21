import random


class Human:
    def __init__(self, name, job=None, car=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def eat(self):
        eat = random.randint(1, 10)
        print(f"Я з'їв {eat}% їжи")
        self.house.food -= eat

    def chill(self):
        print(f"Я відпочиваю")
        self.house.pollution += 2
        self.money -= 5

    def shopping(self):
        self.money -= random.randint(1,10)
        if not self.car.drive(random.randint(1,10)*10):
            print("Пішли в магазин пішки")
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
        self.money += 10
        if self.car != None:
            if not self.car.drive(20):
                print("Я поїхав на роботу")
            else:
                print("Я сходив на роботу")
        else:
            print("Я сходив на роботу")

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
        return f"Холодильник забитий {self.food}%, забудненість {self.pollution}%"



human1 = Human("Serg", job=Job("Викладач", 1000), car=Car("BMW X11"))
human1.work()

# human2 = Human("Anna")
#
# car = Car("BMW X11")
# car.add_passenger(human1, human2)
#
# car.print_passenger()