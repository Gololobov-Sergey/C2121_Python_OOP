import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progress += 0.1
        self.gladness -= 5

    def to_sleep(self):
        print("Я пішов спати")
        self.progress += 0.02
        self.gladness += 3

    def to_chill(self):
        print("Я відпочиваю")
        self.gladness += 5
        self.progress -= 0.1

    def info(self):
        print(f"Рівень навчання {round(self.progress, 2)}")
        print(f"Задоволення     {self.gladness}")
        print()

    def is_alive(self):
        if self.progress > 5:
            print("Ми все вивчили, і закінчили МКА ШАГ")
            self.alive = False
        if self.progress < -0.5:
            print("Ми втратили інтерес до навчання ....")
            self.alive = False
        if self.gladness <= 0:
            print("У мене дипресія")
            self.alive = False

    def live(self, day):
        print(f"День {day} з життя {self.name}")
        print("====================================")
        choice = random.randint(1, 3)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_chill()
        choice2 = random.randint(1, 20)
        if choice2 == 20:
            self.func()  # ДЗ
        self.info()
        self.is_alive()


student = Student("C2121")
for day in range(366):
    if student.alive == False:
        break
    student.live(day)


