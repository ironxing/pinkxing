operations = ["Add", "Subtract", "Divide", "Multiply"]


def is_number(raw_input):
    try:
        float(raw_input)
        return True
    except ValueError:
        return False


go_on = True
while go_on:
    operation = input("Please select a type of calculation: Add/Subtract/Divide/Multiply").capitalize()

    if operation in operations:
        number_input1 = ""
        number_input2 = ""

        number_input1 = input("Please input the first number:")
        while not(is_number(number_input1)):
            number_input1 = input("The input is not a number, please try again. Please input the first number:")

        number_input2 = input("Please input the first number:")
        while not(is_number(number_input2)):
            number_input2 = input("The input is not a number, please try again. Please input the second number:")

        number1 = float(number_input1)
        number2 = float(number_input2)

        if operation == "Add":
            print("Result: " + str(round(number1 + number2, 2)))
        elif operation == "Subtract":
            print("Result: " + str(round(number1 - number2, 2)))
        elif operation == "Divide":
            print("Result: " + str(round(number1 / number2, 2)))
        else:
            print("Result: " + str(round(number1 * number2, 2)))

        go_on = False
    else:
        print("I do not understand the operation you chose, please choose again from Add/Subtract/Divide/Multiply.")





