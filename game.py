import random

def game(score):
    mynumber = random.randint(1, 10)
    promt_list = ["Can you guess the number? Write it down here. It is an integer number between 1-10.",
                "Wanna guess again? It is an integer number between 1-10.",
                "Guess one more time? It is an integer number between 1-10."]
    for i in range(3):
        promt = promt_list[i]
        yourguess = int(input(promt))
        if yourguess == mynumber:
            print("Your are right, awesome!!")
            score += 1
            break

    if score == 0:
        print("Opps, you did not guess it right.")
    else:
        print("Wow! Awesome guess! Your score is " + str(score) + " !")


def wanttocontinue():
    wanttocontinue_input = input("Do you want to continue playing? Y/N").capitalize()
    if wanttocontinue_input == "N":
        return False
    return True

score = 0
play = True
while play:
    starttext = """ Let's play a game!
    I will be thinking about an integer number between 1-10.
    You can guess it 3 times, if you get it right, you will get 1 point.
    Let's start!
    """

    game(score)
    play = wanttocontinue()





