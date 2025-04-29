class Person:
    name = "anonyous"


    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()

p1.changeName("laksh lukhi")
print(p1.name)
print(Person.name)