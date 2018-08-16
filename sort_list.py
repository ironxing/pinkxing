number_list = [2, 6, 3, 4, 8, 99]
sorted_list = []

for i in range(len(number_list)):
    minimal = min(number_list)
    index = number_list.index(minimal)
    del number_list[index]
    sorted_list.append(minimal)

print(sorted_list)




# number = int(input("Please input a number"))
# for i in range(len(number_list)):
#     if number == number_list[i]:
#         print(str(i+1))
#         found = True
#         break
# if not found:
#     print("None")