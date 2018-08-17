def check_letter(word, letter):
    if letter in word:
        indices = [i for i, x in enumerate(word) if x == letter]
        return indices
    else:
        return False


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

word = "INVEITORYI"
length = len(word)

letter = input("Please input a letter.")
on_screen = initial_screen(length)
print(" ".join(on_screen))

counter = 0

on_screen_string = "".join(on_screen)
all_right = check_word(word, on_screen_string)
print(all_right)


while counter < 8 and not all_right:
    update_indices = check_letter(word, letter)
    on_screen = update_on_screen(word, on_screen, update_indices)
    print(" ".join(on_screen))
    all_right = check_word(word, on_screen_string)

#
#
print(a)