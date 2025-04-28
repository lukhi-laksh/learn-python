class Employee:
    coumpany = "ITC"
    name = "laksh"
    sallery = 22
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Coder:
    language = "python"
    def printLanguages(self):
        print(f"out of all of the language here is your language {self.language}")
        
class Programmer(Employee, Coder):
    coumpany = "ITC infotech"
    language = "englsih"
    def showLanguage(self):
        print(f"The name is {self.name} and him feviroute language is {self.language} language")


a = Employee()
b = Programmer()
b.printLanguages()
b.showLanguage()

