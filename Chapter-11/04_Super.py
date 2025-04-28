class Employee:
    def __init__(self):
        print("Constroceter of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constroceter of Programmer")
    b = 2

class Manager(Programmer):
    
    def __init__(self):
        super().__init__()
        super().__init__()
        print("Constroceter of Manager")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)