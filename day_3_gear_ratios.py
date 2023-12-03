# Day 3 (Note: 3.1 did not work with the large input)

# Part 1:

# Input:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.

# Output: sum up all numbers adjacent to a symbol, even diagonally
# i.e. All except 114 (top right) and 58 (middle right). All else sums to 4361.


import re

with open("input.txt") as f:
    all_lines = f.read().splitlines()


    
# Do something to make life easier

valid_symbols = set()

bubble_wrap_line = "."*len(all_lines[0])

all_lines = [bubble_wrap_line] + all_lines + [bubble_wrap_line]

for i, line in enumerate(all_lines):
    
    all_lines[i] = "." + line + "."
    
    symbs = ''.join([char for char in line if not char.isdigit()]).replace(".", "")
    valid_symbols.update(symbs)

print(valid_symbols)

# Now we begin

list_of_nums = []

for i, line in enumerate(all_lines):
    num_in_line = re.findall(r'\d+', line)

    for num in num_in_line:

        #print(f"The num is {num}")
        #print(f"The line is {line}")
        
        start_of_range = line.find(num)-1
        end_of_range = start_of_range + len(num)+1
        # add +1 to look ahead in range

        #look ahead and behind
        if line[start_of_range] in valid_symbols or line[end_of_range] in valid_symbols:
            list_of_nums.append(int(num))
            #print(f"{num} made it onto the list!")
            continue
        
        #Look up and diagonal
        prev_line_chunk = all_lines[i-1][start_of_range:end_of_range+1]
        mod_plc = ''.join([i for i in prev_line_chunk if not i.isdigit()])
        mod_plc = mod_plc.replace(".", "")
        
        #Look down and diagonal
        next_line_chunk = all_lines[i+1][start_of_range:end_of_range+1]
        mod_nlc = ''.join([i for i in next_line_chunk if not i.isdigit()])
        mod_nlc = mod_nlc.replace(".", "")

        #print(f"prev_line_chunk mod_plc is {prev_line_chunk} and next_line_chunk is {next_line_chunk}")
        #print(f"mod_plc is {mod_plc} and mod_nlc is {mod_nlc}")

        if len(mod_plc) or len(mod_nlc) > 0:
            list_of_nums.append(int(num))
            # print(f"{num} made it onto the list!")
            
print(sum(list_of_nums))


# Part 2

