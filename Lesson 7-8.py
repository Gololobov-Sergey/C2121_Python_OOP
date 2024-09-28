class Human:
    height = 170
    progress = 20
    def info(self):
        print("I`m human")

class Student(Human):
    progress = 15

    def info(self):
        print("I`m student")

class Worker(Human):
    salary = 1000


# stud = Student()
# worker = Worker()
#
# print(stud.height)
# print(worker.height)
#
# print(stud.progress)
# print(worker.progress)
# print(worker.salary)
#
# stud.info()


# class Grandparent:
#     height = 170
#     age = 60
#     home = "Будинок в селі"
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 100
#
#     def __init__(self):
#         print(self.height)
#         print(self.age)
#         print(self.home)
#
# child = Child()

# class SuperTest:
#     def _test1(self):
#         print("Test1")
#
#     def test2(self):
#         self._test1()
#         self.__test3()
#
#
#     def __test3(self):
#         print("Test3")
#
#
# class Test(SuperTest):
#
#     def print(self):
#         self.test2()
#         self._test1()
#         self.__test3()
#
# t = SuperTest()
# t._test1()
# t.__test3()
#
# tt = Test()
# tt.print()

# class Student:
#     def __init__(self, age):
#         self.__age = age
#
#     def getAge(self):
#         return self.__age
#
#     def setAge(self, age):
#         if age < 0 or age > 100:
#             return
#         self.__age = age
#
#
# st = Student(15)
# print(st.getAge())
# st.setAge(20)
# print(st.getAge())

class Class1:
    pass

class Class2:
    pass

class Class3(Class1, Class2):
    pass


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128

    def calc(self):
        print("Calculate..")

class Display:
    def __init__(self):
        super().__init__()
        self.diagonal = "7'"
    def display(self):
        print("Displayed....")


class MobilePhone(Display, Computer):
    def info(self):
        print(self.memory)
        print(self.diagonal)

phone = MobilePhone()
phone.calc()
phone.display()
phone.info()