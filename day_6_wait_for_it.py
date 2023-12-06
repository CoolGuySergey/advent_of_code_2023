# Day 6

# A given race lasts a fixed amount  of time.
# Winning boat is the one that goes the furthest within that time.

# Eaach boat has a button.
# Holding it down charges the boat, and releasing the button allows the boat to move.
# Boats move faster if their button was held longer
# But time spent holding the button counts against the total race time.
# You can only hold the button at the start of the race. i.e. no movement until you release

# This document describes 3 races:

# Time:      7  15   30
# Distance:  9  40  200

# The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
# The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
# The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.

# For 1 millisecond you spend at the beginning of the race holding down the button
# the boat's speed increases by 1 millimeter per millisecond.

# So, because the first race lasts 7 milliseconds, you only have a few options:

# 0 ms hold, 0mm travelled
# 1 ms hold, 1 mm / ms for 6 ms i.e. 6 mm travelled
# 2 ms hold, 2 mm / ms for 5 ms i.e. 10 mm travelled
# 3 ms hold, 3 mm / ms for 4 ms i.e. 12 mm travelled
# 4 ms hold. 4 mm / ms for 3 ms i.e. 12 mm travelled
# 5 ms hold, 5 mm / ms for 2 ms i.e. 10 mm travelled
# 6 ms hold, 6 mm / ms for 1 ms i.e. 6 mm travelled
# 7ms hold, 0mm travelled

# In the first race, you could hold the button for at least 2 ms and at most 5 ms
# i.e. total of 4 different ways to win.

# In the second race, you could hold the button for at least 4 ms and at most 11 ms
# i.e. total of 8 different ways to win.

# In the third race, you could hold the button for at least 11 ms and at most 19 ms
# i.e. total of 9 different ways to win. (i.e. you have to EXCEED the record to win)

# Determine the number of ways you can beat the record in each race;
# Then multiply these values together. In this example, you get 288 (4 * 8 * 9).

#================================================================================
# Ingestion

import re

with open("input.txt") as f:
    all_lines  = f.read().splitlines()

time_list = [int(time) for time in all_lines[0].split(" ") if time.isdigit()]
dist_list = [int(dist) for dist in all_lines[1].split(" ") if dist.isdigit()]

race_list = list(zip(time_list, dist_list))

#================================================================================
# Functions

def extreme_record_val_handler(record_val, total_time):

    if record_val == 0:
        return total_time - 2

    if record_val == total_time - 1:
        return total_time - 4

    return None

def dist_calculator(down_time, total_time):
    return (down_time * (total_time - down_time))

def min_down_time_finder(record_val, total_time):

    down_time = 2
    dist = 0
    
    while dist <= record_val:
        dist = dist_calculator(down_time, total_time)
        down_time += 1

    return down_time-1

def max_down_time_finder(record_val, total_time):

    down_time = total_time-2
    dist = dist_calculator(down_time, total_time)
    
    while dist <= record_val:
        
        down_time -= 1
        dist = dist_calculator(down_time, total_time)
        
        if dist == record_val:
            down_time -= 1
            break
        
    return down_time

def multiply_list_elements(lst):
    result = 1
    for element in lst:
        result *= element
    return result

#================================================================================
# Main

ans_list = []

for race in race_list:
    
    total_time = race[0]
    record_val = race[1]

    if extreme_record_val_handler(record_val, total_time) == None:

        min_down_time = min_down_time_finder(record_val, total_time)
        max_down_time = max_down_time_finder(record_val, total_time)
        ans = max_down_time - min_down_time + 1

        ans_list.append(ans)

    else:
        ans = extreme_record_val_handler(record_val, total_time)
        ans_list.append(ans)
    
multiply_list_elements(ans_list)

#================================================================================
# Part 2

# You realise there's only one race - ignore the spaces between the numbers on each line.
# The total time is now 71530 ms and the record distance is 940200 mm.
# min down time is 14 ms and max is 71516 ms
# A total of 71503 ways

# Ans: just edited the input and the code still runs in less than a second. Yayyy!!
