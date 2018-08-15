operations = ["Add", "Subtract", "Divide", "Multiply"]

go_on = True
while go_on:
    operation = input("Please select a type of calculation: Add/Subtract/Divide/Multiply").capitalize()

    if operation in operations:
        try:
            first_number = float(input("Please input the first number:"))
        except ValueError:
            print("Please input a number.")
            continue

        try:
            second_number = float(input("Please input the second number:"))
        except ValueError:
            print("Please input a number.")

        if operation == "Add":
            print(first_number + second_number)
        elif operation == "Subtract":
            print(first_number - second_number)
        elif operation == "Divide":
            print(first_number / second_number)
        else:
            print(first_number * second_number)

        go_on = False
    else:
        print("I do not understand the operation you chose, please choose again from Add/Subtract/Divide/Multiply.")





("I do not understand, can you select the calculation from the list? Add/Subtract/Divide/Multiply")

