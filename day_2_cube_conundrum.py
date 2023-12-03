# Part 1

# Cubes in bag.
# Semicolons separate different random draws (with replacement)
# Games separate different bags


# Input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# What is the sum of the IDs of all the games that could be played w/ bag of 12 red, 13 green, and 14 blue?

# Output:
# Games 1, 2, and 5 would've been possible i.e. 8

import re

with open("input.txt") as f:
    all_games = f.read().splitlines()

list_of_id = []

for game_id, game in enumerate(all_games):
    game_pass = True

    all_samples = game.split(": ")[1].split("; ")

    for sample in all_samples:
        sample_pass = True
              
        all_counts = sample.split(", ")
        
        for count in all_counts:
            if "red" in count and int(count.split(" ")[0]) > 12:
                sample_pass = False
                break
            if "green" in count and int(count.split(" ")[0]) > 13:
                sample_pass = False
                break
            if "blue" in count and int(count.split(" ")[0]) > 14:
                sample_pass = False
                break
            
        if sample_pass == False:
            game_pass = False
            break

    if game_pass == False:
        continue
    
    game_pass = True
    list_of_id.append(game_id+1)

print(sum(list_of_id))


#=========================================================================================================

# Part 2

# Input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

# What is the fewest number of cubes of each color that could have been in the bag to make each game possible?
# 4 red, 2 green, and 6 blue cubes for Game 1
# 1 red, 3 green, and 4 blue cubes for Game 2

# Should output those numbers multiplied within and summed between games
# i.e. 48, 12, 1560, 630, and 36 sums up to 2286.

import re

with open("input.txt") as f:
    all_games = f.read().splitlines()


sum_of_magic_num = 0

for game in all_games:
    all_samples = re.split(': |; |, ', game)
    
    red_max = max([int(item.split(" ")[0]) for item in all_samples if 'red' in item])
    green_max = max([int(item.split(" ")[0]) for item in all_samples if 'green' in item])
    blue_max = max([int(item.split(" ")[0]) for item in all_samples if 'blue' in item])

    magic_num = int(red_max) * int(green_max) * int(blue_max)

    sum_of_magic_num += magic_num

print(sum_of_magic_num)
