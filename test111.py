def backwards():
    input_string = input("Please type in some input.").upper()
    output = ""
    length = len(input_string)

    for i in range(-1, -length, -1):
        output += input_string[i]
    output += input_string[0]
    print(output)

backwards()