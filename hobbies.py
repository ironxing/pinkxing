go_on = True
hobbies = []

while go_on:
    hobby = input("What do you like to do?")
    if hobby == "stop":
        go_on = False
        break
    hobbies.append(hobby)

hobbies_string = ""

for hobby in hobbies:
    if not hobbies_string:  # dd
        hobbies_string = hobby
    else:
        hobbies_string += ", " + hobby

print("Okay. Hobbies are " + hobbies_string + ".")


