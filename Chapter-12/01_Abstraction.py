class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False 
    def start(self, ):
        self.clutch = True
        self.acc = True
        print("Car is started...")

mycar = Car()
mycar.start()