class Employee:
    sallery = 20000
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.sallery + (self.increment * self.sallery)
     
    
e = Employee() 

print(e.salaryAfterIncrement)