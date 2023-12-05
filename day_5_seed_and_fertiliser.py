# Day 5

# Part 1

# Input

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

# Each line within a map contains: the destination range start, the source range start, and the range length.

# find the lowest location number that corresponds to any of the initial seeds.

# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

# So, the lowest location number in this example is 35.

#========================================================================================================
# INGESTION

import re

with open("input.txt") as f:
    all_lines  = f.read().splitlines()

seed_list = re.split(": | ", all_lines[0])[1:]

#create list of 7 empty lists
map_list = [[],[],[],[],[],[],[]]

i = 0
for line in all_lines[3:]:
    if "map" in line:
        i += 1
        continue
    if not line:
        continue
    map_list[i].append(line)

#========================================================================================================
# FUNCTIONS

def out_of_range_finder(in_val, in_lists):

    min_of_range = min([int(in_list.split(" ")[1]) for in_list in in_lists])
    max_of_range = max([int(in_list.split(" ")[1]) + int(in_list.split(" ")[2]) for in_list in in_lists])

    if in_val < min_of_range or in_val > max_of_range:
        return True
    else:
        return False

def out_val_calculator(in_val, in_lists):

    out_val = None
    
    for in_list in in_lists:

        min_range = int(in_list.split(" ")[1])
        max_range = int(in_list.split(" ")[1]) + int(in_list.split(" ")[2])
        
        if in_val < min_range or in_val > max_range:
            continue

        if in_val == min_range:
            return int(in_list.split(" ")[0])

        out_val = in_val + (int(in_list.split(" ")[0]) - int(in_list.split(" ")[1]))

    if out_val == None:
        return in_val
        
    return out_val

def main_calculator(in_val, in_lists):
    
    if out_of_range_finder(in_val, in_lists):
        return in_val

    out_val = out_val_calculator(in_val, in_lists)
    
    return out_val

#========================================================================================================
# MAIN

ans_list = []

for seed in seed_list:

    cur_in_val = int(seed)
    
    for m in map_list:
        
        next_in_val = main_calculator(cur_in_val, m)

        cur_in_val = next_in_val
        
    ans_list.append(cur_in_val)

print(min(ans_list))
