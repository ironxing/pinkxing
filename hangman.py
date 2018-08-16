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
    return on

def update_on_screen(word, on_screen, update_indices):
    for index in update_indices:
        on_screen[index] = word[index]
    return on_screen


word = "INVEITORYI"
length = len(word)

letter = input("Please input a letter.")
print_initial_screen(length)
on_screen = initial_screen()
update_indices = check_letter(word, letter)

new_onscreen = update_on_screen(word, on_screen, update_indices)
print(new_onscreen)


print(a)