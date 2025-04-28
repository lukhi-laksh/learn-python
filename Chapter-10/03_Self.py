class Employee:
    langauge = "python"
    salary = 30000

    def getinfo(self):
        print(f"The langauge is {self.langauge}, and sallery is {self.salary}")

    @staticmethod
    def greet():
        print("this is my static method")

laksh = Employee()

laksh.getinfo()
# Employee.getinfo(laksh)
laksh.greet()