import random

def game():
    print("you are playing the game..")
    score = random.randint(2, 50)
    #fetch the high score
    with open("Problem-11.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score is: {score}")
    if(score > hiscore):
        #write new scorein the problem-11 file
        with open("Problem-11.txt", "w") as f:
            f.write(str(score))
    return score    


game()
