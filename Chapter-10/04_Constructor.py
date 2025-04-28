class Employee:
    langauge = "python"
    salary = 30000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.langauge = language

        print(f"my name is {name}, and my sallary is {salary}, and language is {language}")
        print("i am init method")

    def getinfo(self):
        print(f"The langauge is{self.name} {self.langauge}, and sallery is {self.salary}")

    @staticmethod
    def greet():
        print("this is my static method")

laksh = Employee("harsh", 4000, "php")
laksh.name = "laksh"
laksh.getinfo()
laksh.greet()

print(laksh.salary, laksh.salary, laksh.name)
