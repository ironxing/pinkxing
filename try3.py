def check_word(word, on_screen_string):
    if word == on_screen_string:
        return True
    else:
        return False

word = "Apple".upper()
on_screen = ["A", "P", "P", "L", "E"]
on_screen_string = "".join(on_screen)
all_right = check_word(word, on_screen_string)
print(all_right)