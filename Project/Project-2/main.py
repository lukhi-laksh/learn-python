import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess a Number: "))
    if(a > n):
        print("Lower Number please")
    elif(a < n):
        print("Higher number please")
    else:
        print(f"Got it! you won in {guesses} attempt. Guesses number is {n}")
    
        