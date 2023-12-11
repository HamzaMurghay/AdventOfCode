sstring = """Time:        54     94     65     92
Distance:   302   1476   1029   1404"""

# sstring = """Time:      7  15   30
# Distance:  9  40  200"""

max_time = int(''.join(sstring.splitlines()[0].split()[1:]))
record_distance = int(''.join(sstring.splitlines()[1].split()[1:]))

no_of_ways_to_win = 0
for seconds_held in range(max_time):
    seconds_travelled = max_time - seconds_held
    final_distance = seconds_travelled * seconds_held
    if final_distance > record_distance:
        no_of_ways_to_win += 1

print(no_of_ways_to_win)
