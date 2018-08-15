go_on = True
hobbies = []

while go_on:
    hobby = input("What do you like to do?")
    if hobby == "stop":
        go_on = False
        break
    hobbies.append(hobby)

print("Okay. Hobbies are " + ', '.join(hobbies) + ".")


