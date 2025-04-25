def large(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return("num1 is large one")
    elif(num2 > num1 and num2 > num3):
        return("num2 is large one")
    else:
        return("num3 is large one")

print(large(88, 57, 55))
