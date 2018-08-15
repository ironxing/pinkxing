operation = input("Please select a type of calculation: Add/Subtract/Divide/Multiply").capitalize()
first_number = float(input("Please input the first number:"))
second_number = float(input("Please input the second number:"))

if operation == "Add":
    print(first_number + second_number)
elif operation == "Subtract":
    print(first_number - second_number)
elif operation == "Divide":
    print(first_number / second_number)
elif operation == "Multiply":
    print(first_number * second_number)
else:
    print("")

