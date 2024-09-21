class Human:
    def __init__(self, name, job=None, car=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job


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
            print("Подорож не можлива, не вистачає пального")
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



human1 = Human("Serg", Job("Викладач", 1000))
human2 = Human("Anna")

car = Car("BMW X11")
car.add_passenger(human1, human2)

car.print_passenger()