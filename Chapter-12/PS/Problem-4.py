class Car:
    wheels = 4  

    def __init__(self):
        self._brand = None

    @classmethod
    def display_wheels(cls):
        print(f"All cars have {cls.wheels} wheels.")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

c = Car()
c.wheels = 6      
c.brand = "Toyota"
print(c.brand)    
c.display_wheels()
