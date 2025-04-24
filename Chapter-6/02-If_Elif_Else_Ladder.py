age = int(input("Enter Your Age: "))

if(age >= 18):
    print("You are above age of consent")
    print("Good for you")
elif(age < 0):
    print("You are entering invalid age")
elif(age == 0):
    print("You are entering 0 which is not valid age")
else:
    print("You are below age of consent")

print("End of program")