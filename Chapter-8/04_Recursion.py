'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

def fectorial(n):
    if(n==0 or n==1):
        return 1
    return n * fectorial(n -1)

n = int(input("Enter number for call find fectorial: "))
print(f"the fectorial of this number is: {fectorial(n)}")