# Part1

# Input:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# Should output:

# The sum of 12, 38, 15, and 77 i.e. 142

import re

with open("input.txt") as f:
    all_lines  = f.read().splitlines()

sum_of_magic_num = 0

for line in all_lines:
    first_digit = re.findall(r'\d', line)[0]
    last_digit = re.findall(r'\d', line)[-1]

    magic_num = first_digit + last_digit
    sum_of_magic_num += int(magic_num)

print (sum_of_magic_num)

#=======================================================

# Part 2

# Input:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# Should output:

# The sum of 29, 83, 13, 24, 42, 14, and 76 i.e. 281

number_dict = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine"
}


import re

with open("input.txt") as f:
    all_lines  = f.read().splitlines()

sum_of_magic_num = 0

for line in all_lines:

    # Added step: use dict to expose  all spellt out nums to re
    for text_num, bs_num in number_dict.items():
        line = line.replace(text_num, bs_num)

    first_digit = re.findall(r'\d', line)[0]
    last_digit = re.findall(r'\d', line)[-1]

    magic_num = first_digit + last_digit
    sum_of_magic_num += int(magic_num)

print (sum_of_magic_num)
