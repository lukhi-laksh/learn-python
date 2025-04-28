class calculator:
    def __init__(self, n):
        self.n = n

    
    def sequre(self):
        print(f"the squre is {self.n * self.n}")
    def cube(self):
        print(f"the squre is {self.n * self.n * self.n}")
    def sequreRoot(self):
        print(f"the squre is {self.n**1/2}")
            

a = calculator(4)

a.sequre()
a.cube()
a.sequreRoot()
        
    