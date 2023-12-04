# Day 4

# Part 1

# Input: a list of winning numbers and then a list of numbers you have.

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# Which of the numbers you have appear in the list of winning numbers?
# The first match makes the card worth 1 point and each match after the first x2 the point value of that card.

# In card 1, 83, 86, 17, and 48 are winning numbers! That means card 1 is worth 8 points
# Card 2 has two winning numbers (61 and 32), so it is worth 2 points.
# Card 3 has two winning numbers (21 and 1), so it is worth 2 points.
# Card 4 has one winning number (84), so it is worth 1 point.
# Cards 5 and 6 have no matches

# Output: sum of all points, i.e. 13

import re

with open("input.txt") as f:
    all_cards  = f.read().splitlines()

score = 0

for card in all_cards:

    winning_nums, nums_u_have = card.split(" | ")
    winning_nums = winning_nums.split(": ")[1]
    winning_nums = winning_nums.split(" ")
    nums_u_have = re.split(' ', nums_u_have)

    winning_nums = [w for w in winning_nums if w != ""]
    nums_u_have = [h for h in nums_u_have if h != ""]

    #print(winning_nums)
    #print(nums_u_have)
    
    overlap = set(winning_nums).intersection(nums_u_have)
    
    if not overlap:
        continue
    
    score += 2 ** (len(overlap)-1)
    
print(score)


# Part 2

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

# This time, cards cause you to win more scratchcards equal to the number of winning numbers you have.

# Specifically, you win copies of the scratchcards below the winning card equal to the number of matches.
# Copies of scratchcards are scored like the original scratchcards and have the same card number
# This process repeats until none of the copies cause you to win any more cards.

# So:
# Card 1 has 4 matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
# Card 2 and its 1 copy have 2 matching numbers, so you win 2 copies each of cards 3 and 4.
# Card 3 and its 3 copies have 2 matching numbers, so you win 4 copies each of cards 4 and 5.
# Card 4 and its 7 copies have 1  matching number, so you win 8 copies of card 5.
# Card 5 and its 13 copies have 0 matching numbers and win no more cards.
# Card 6 has 0 matching numbers and wins no more cards.

# You end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3
# 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6.
# In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

# Output: how many total scratchcards do you end up with?

with open("input.txt") as f:
    all_cards  = f.read().splitlines()

# card_tally = {key:1 for key in list(range(1, len(all_cards)))}

card_tally = [1] * len(all_cards)
              
for i, card in enumerate(all_cards):

    #print(i)
    
    winning_nums, nums_u_have = card.split(" | ")
    winning_nums = winning_nums.split(": ")[1]
    winning_nums = winning_nums.split(" ")
    nums_u_have = re.split(' ', nums_u_have)

    winning_nums = [w for w in winning_nums if w != ""]
    nums_u_have = [h for h in nums_u_have if h != ""]

    #print(winning_nums)
    #print(nums_u_have)

    repeats = 0
    while repeats < card_tally[i]:

        no_of_overlap = len(set(winning_nums).intersection(nums_u_have))
        #print(no_of_overlap)

        affected_indices = list(range(i+1, i+1+no_of_overlap))
        #print(f"affected indices are {affected_indices}")

        #update values at specified indices
        for index in affected_indices:
            card_tally[index] += 1
            #print(card_tally)
        
        repeats += 1

print(sum(card_tally))
