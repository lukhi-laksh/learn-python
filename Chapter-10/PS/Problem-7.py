class Student():
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3      
        print(f"name {name} is mark average is {(self.sub1 + self.sub2 + self.sub3) /3}")

s = Student("laksh", 33, 33, 36)