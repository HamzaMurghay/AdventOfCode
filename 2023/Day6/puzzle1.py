sstring = """Time:        54     94     65     92
Distance:   302   1476   1029   1404"""

# sstring = """Time:      7  15   30
# Distance:  9  40  200"""

time_list = [int(time) for time in sstring.splitlines()[0].split()[1:]]
distance_list = [int(record_distance) for record_distance in sstring.splitlines()[1].split()[1:]]

final_product = 1

for race_no in range(4):
    no_of_ways_to_win = 0
    for seconds_held in range(time_list[race_no]):
        seconds_travelled = time_list[race_no] - seconds_held
        final_distance = seconds_travelled * seconds_held
        if final_distance > distance_list[race_no]:
            no_of_ways_to_win += 1
    final_product *= no_of_ways_to_win

print(final_product)
