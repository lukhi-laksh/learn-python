class Complex():
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
    def __mul__(self, num2):
        newReal = self.real * num2.real
        newImg = self.img * num2.img
        return Complex(newReal, newImg)
    

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(5, 7)
num2.showNumber()  

print("for sum")
num3 = num1 + num2
num3.showNumber()

print("for substract")
num3 = num1 - num2
num3.showNumber()

print("for multiplication")
num3 = num1 * num2
num3.showNumber()
