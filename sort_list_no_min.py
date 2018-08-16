number_list = [20, 6, 3, 4, 8, 99]
sorted_list = []

for number in number_list:
    index = number_list.index(number) + 1
    remain_numbers = number_list[index:]
    print(remain_numbers)
    for number2 in remain_numbers:
        if number > number2:
            break
        else

#
# while len(number_list) != 0:
#
#     for number in number_list:
#         print(number)
#         if number_current > number:
#             break
#         else:
#             minimal = number_current

# print(minimal)
