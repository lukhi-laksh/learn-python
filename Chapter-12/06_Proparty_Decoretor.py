class Student:
    def __init__(self, phy, cam, math):
        self.phy = phy
        self.cam = cam
        self.math = math
        

    # def calpercentage(self):
    #     self.percentage = str((self.phy + self.cam + self.math) / 3) + " %"

    @property
    def percentage(self):
        return str((self.phy + self.cam + self.math) / 3) + " %"

stu1 = Student(55,55,55)
print(stu1.percentage)

stu1.phy = 68
print(stu1.percentage)