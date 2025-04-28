import random

def game():
    print("you are playing game....")
    score = random.randint(1, 50)
    with open("Problem-12.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore=(int(hiscore))
        else:
            hiscore = 0
        print(f"Your score is {score}")
    if(hiscore < score):
        with open("Problem-12.txt", "w") as f:
            f.write(str(score))
game()