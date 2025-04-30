class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism in action
def make_animal_speak(animal):
    animal.speak()

a = Animal()
d = Dog()
c = Cat()

make_animal_speak(a) 
make_animal_speak(d) 
make_animal_speak(c) 
