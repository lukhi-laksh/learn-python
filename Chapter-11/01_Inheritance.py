class Employee:
    coumpany = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     coumpany = "ITC infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
#     def showLanguage(self):
#         print(f"The name is {self.name} and him feviroute language is {self.language} language")

class Programmer(Employee):
    coumpany = "ITC infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and him feviroute language is {self.language} language")


a = Employee()
b = Programmer()

print(a.coumpany)
print(b.coumpany)