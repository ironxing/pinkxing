# for i in range(11):
#     print(i)
#
# for i in range(10, 20, 2):
#     print(i)
#
# for i in range(20, 10, -2):
#     print(i)
#
# names = ['a', 'b', 'c']
# for name in names:
#     print("Hi, " + name)
#     print("If I get a cat, I will call it " + ",".join(names))

# counter = 5
# while counter > 0:
#     print(counter)
#     counter -= 1

# counter = 30
# while counter > 0:
#     residual = counter % 4
#     if residual == 0:
#         print(counter)
#     counter -= 1

# deci_amount = float(input("Please input deciliter amount:"))
# cup_amount = str(round(deci_amount / 2.37, 2))
# print(str(deci_amount)+ "deciliters is equivalent to " + cup_amount + " cups.")

found = False
number_list = [2, 6, 3, 4, 8]

number = int(input("Please input a number"))
for i in range(len(number_list)):
    if number == number_list[i]:
        print(str(i+1))
        found = True
        break
if not found:
    print("None")



