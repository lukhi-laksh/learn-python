'''
1 for snak
0 for gun
-1 for water
'''

computer = -1
you = int(input("Enter your choice: "))

if(computer == 1 and you == 0):
    print("You win!")
elif(computer == 0 and you == -1):
    print("you win")
elif(computer == -1 and you == 1):
    print("you win")
else:
    print("computer win")