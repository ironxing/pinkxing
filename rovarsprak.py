def rovarsprak(input):
    vowel = ["a", "e", "i", "o", "u"]

    if len(input) == 1:
        if input.lower() not in vowel:
            return input + "o" + input
        else:
            return input 
    else:
        if input[0].lower() not in vowel:
            return input[0] + "o" + input[0] + rovarsprak(input[1:])
        else:
            return input[0] + rovarsprak(input[1:])

a = rovarsprak("Apple")
print(a)