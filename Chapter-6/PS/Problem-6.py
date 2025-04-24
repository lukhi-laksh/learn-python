marks = int(input("Enter Your marks"))

if(marks <= 100 and marks >= 90):
    print("your gread is EX")
elif(marks <= 90 and marks <= 80):
    print("your gread is a")
elif(marks <= 80 and marks <= 70):
    print("your gread is b")
elif(marks <= 70 and marks <= 60):
    print("your gread is c")
elif(marks <= 0):
    print("low gread")
else:
    print("Invalid marks")
    
