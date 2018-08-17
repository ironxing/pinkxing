import random

def check_letter(word, letter):
    if letter in word:
        indices = [i for i, x in enumerate(word) if x == letter]
        return indices
    else:
        indices = []
        return indices


def initial_screen(length):
    on_screen = []
    for i in range(length):
        on_screen.append("_")
    return on_screen


def update_on_screen(word, on_screen, update_indices):
    for index in update_indices:
        on_screen[index] = word[index]
    return on_screen


def check_word(word, on_screen_string):
    if word == on_screen_string:
        return True
    else:
        return False

def pick_random_word(word_list):
    random_index = random.randint(0, 4)
    word = word_list[random_index]
    return word


word_list = ["INVENTORY", "APPLE", "GAME", "PINK", "PYTHON"]
word = pick_random_word(word_list)
length = len(word)
go_on = True

while go_on:
    on_screen = initial_screen(length)
    print(" ".join(on_screen))

    counter = 0
    on_screen_string = "".join(on_screen)
    all_right = check_word(word, on_screen_string)

    while counter < 8 and not all_right:
        letter = input("Please input a letter.").upper()
        update_indices = check_letter(word, letter)
        on_screen = update_on_screen(word, on_screen, update_indices)
        print(" ".join(on_screen))
        all_right = check_word(word, "".join(on_screen))
        counter +=1

    if all_right:
        print("Congrats, you guessed right!!")
    else:
        print("Too bad, you did not guess right :(")

    go_on_string = input("Wanna play again? Y/N").upper()
    if go_on_string == "N":
        go_on = False
