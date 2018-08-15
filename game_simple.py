score = 0
print("Let's play a game!")
print("I will be thinking about an integer number between 1-10.")
print("You can guess it 3 times, if you get it right, you will get 1 point.")
print("Let's start!")

mynumber = 1
for i in range(3):
    yourguess = int(input("Can you guess the number? Write it down here. It is an integer number between 1-10."))
    if yourguess == mynumber:
        print("Your are right, awesome!!")
        score += 1
        break

if score == 0:
    print("Opps, you did not guess it right.")
else:
    print("Wow! Awesome guess! Your score is " + str(score) + " !")





