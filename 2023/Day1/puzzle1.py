sstring = "Insert puzzle input here"

final_sum = 0
first_dig = -1
last_dig = -1
digit_count = 0

for char in sstring:

    if char.isdigit():
        digit_count += 1
        if first_dig == -1:
            first_dig = char
        else:
            last_dig = char

    if char == "\n":
        if digit_count == 1:
            last_dig = first_dig
        final_sum += int(first_dig + last_dig)
        first_dig = -1
        last_dig = -1
        digit_count = 0

print(final_sum)
