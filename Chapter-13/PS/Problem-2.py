class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary


    def showDetails(self,):
        print(self.role, self.department, self.salary)

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginiear", "it", 75000)

e = Engineer("laksh lukhi", 56)
e.showDetails()