def check_letter(word, letter):
    if letter in word:
        indices = [i for i, x in enumerate(word) if x == letter]
        return indices
    else:
        return False

a = check_letter("INIENTORY", "I")
print(a)


