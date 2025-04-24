a = int(input("Enter Your Number: "))

#if statement number 1
if(a%2==0):
    print("a is even")
#end of statement number 1
    
#if statement number 2
if(a >= 18):
    print("You are above age of consent")
    print("Good for you")
elif(a < 0):
    print("You are entering invalid age")
else:
    print("You are below age of consent")
#end of statement number 2
    
print("End of program")