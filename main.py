class Student:
    count_of_student = 0
    def __init__(self, name, age=15):
        self.name = name
        self.age = age
        print("Hi!")
        Student.count_of_student += 1

    def __str__(self):
        return f"Я {self.name}, мені {self.age} років"

    # def info(self):
    #     print(f"Я {self.name}, мені {self.age} років")

    def __del__(self):
        print(f"Я {self.name}, і я пішов")
        Student.count_of_student -= 1

    def __len__(self):
        return self.age

    def grow(self, delta=1):
        if self.age + delta > 100:
            print("Error Age")
            return
        self.age += delta



print(Student.count_of_student)

Anton = Student(name="Anton")
print(Anton.age)
Anton.grow(10)
Kirill = Student(name="Kirill", age=17)
print(Kirill.age)

print(Student.count_of_student)

print(Anton)
print(Kirill)

print(len(Anton))