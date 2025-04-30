class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bhou bhou")

d = Dog()

d.bark()

    