import re

sstring = "Insert puzzle input here"

numbers_spelt = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight":  8, "nine":  9}

final_sum = 0
first_dig = -1
last_dig = -1

for line in sstring.splitlines():
    num_spelt_indices = {}
    num_integers_list = {}

    for num in numbers_spelt:
        if line.count(num) > 1:
            for repeat in re.finditer(num, line):
                num_spelt_indices.update({repeat.start(): num})
        elif line.count(num) == 1:
            num_spelt_indices.update({line.index(num): num})

    for char in line:
        if char.isdigit():
            if line.count(char) > 1:
                for repeat in re.finditer(char, line):
                    num_integers_list.update({repeat.start(): char})
            elif line.count(char) == 1:
                num_integers_list.update({line.index(char): char})

    if num_spelt_indices and not num_integers_list:
        first_spelt_number_index = min(list(num_spelt_indices.keys()))
        last_spelt_number_index = max(list(num_spelt_indices.keys()))

        first_dig = str(numbers_spelt[num_spelt_indices[first_spelt_number_index]])
        last_dig = str(numbers_spelt[num_spelt_indices[last_spelt_number_index]])
    elif num_integers_list and not num_spelt_indices:
        first_actual_number_index = min(list(num_integers_list.keys()))
        last_actual_number_index = max(list(num_integers_list.keys()))

        first_dig = str(num_integers_list[first_actual_number_index])
        last_dig = str(num_integers_list[last_actual_number_index])

    elif num_integers_list and num_spelt_indices:
        first_spelt_number_index = min(list(num_spelt_indices.keys()))
        last_spelt_number_index = max(list(num_spelt_indices.keys()))

        first_actual_number_index = min(list(num_integers_list.keys()))
        last_actual_number_index = max(list(num_integers_list.keys()))

        if first_spelt_number_index < first_actual_number_index:
            first_dig = str(numbers_spelt[num_spelt_indices[first_spelt_number_index]])
        else:
            first_dig = str(num_integers_list[first_actual_number_index])

        if last_spelt_number_index > last_actual_number_index:
            last_dig = str(numbers_spelt[num_spelt_indices[last_spelt_number_index]])
        else:
            last_dig = str(num_integers_list[last_actual_number_index])

    elif not num_integers_list and not num_spelt_indices:
        first_dig = last_dig = '0'

    final_sum += int(first_dig+last_dig)

print("SUM: ", final_sum)
