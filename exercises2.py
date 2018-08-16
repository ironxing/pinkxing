import random


def person_input(name, home_town, special_skill):
    return "This is " + name + " of " + home_town + ", " + "undefeated in " + special_skill + " !"


def calc_tip(meal_price):
    if meal_price > 100:
        return meal_price * 0.05
    else:
        return meal_price * 0.1


def fortune_cookie():
    fortunes = ["a", "b", "c", "d"]
    rand_index = random.randint(0, 3)
    return fortunes[rand_index]


def count_number(start_num, end_num):
    result = ""
    for i in range(start_num, end_num+1, 1):
        if not result:
            result += str(i)
        else:
            result += "," + str(i)
    return result


def backwards():
    input_string = input("Please type in some input.").upper()
    output = ""
    length = len(input_string)

    for i in range(-1, -length, -1):
        output += input_string[i]
    output += input_string[0]
    print(output)






print(person_input("Xing", "Beijing", "BJJ"))
tip = calc_tip(30)
print(tip)
print(fortune_cookie())
print(count_number(1, 4))
backwards()