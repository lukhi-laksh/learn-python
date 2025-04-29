class Car():
    def __init__(self, type):
        self.type = type

    @staticmethod
    def startMethod():
        print("car is started")

    @staticmethod
    def stop():
        print("Car is stop")   

class toyotaCar(Car):
    def __init__(self, type, name):
        super().__init__(type)
        print(name)

Car1 = toyotaCar("electric", "seller")
print(Car1.type)