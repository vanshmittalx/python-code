import random
def highscore():
    newScore = random.randint(1,100)
    print(f"your score: {newScore}")
    with open("highscores.txt") as f:
        score = f.read()
        print(f"highscore: {score}")
    if newScore > int(score) or score == "":
        with open("highscores.txt",'w'):
            print(f"new highscore: {newScore}")
highscore()