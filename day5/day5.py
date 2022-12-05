import re

filename = 'data/day5_input1.txt'

header_passed = False
with open(filename) as f:
    for index, line in enumerate(f):
        if index == 0:
            header_length = len(line)
            num_stacks = int(header_length / 4)
            stacks = [[] for _ in range(num_stacks)]
        if len(line) == header_length and not header_passed:
            indexes = [pos + 1 for pos, char in enumerate(line) if char == '[']
            for i in indexes:
                stack_no = int((i - 1) / 4)
                stacks[stack_no].append(line[i])
        elif not header_passed:
            header_passed = True
        elif header_passed and len(line) > 1:
            move = int(re.search('move (\d+)', line).group(1))
            stack_from = int(re.search('from (\d+)', line).group(1)) - 1
            stack_to = int(re.search('to (\d+)', line).group(1)) - 1
            stacks[stack_to] = stacks[stack_from][0:move] + stacks[stack_to] # Part 1 = add [::-1] after first array
            stacks[stack_from] = stacks[stack_from][move:]

top_of_stacks = [s[0] for s in stacks]

result = ""
for t in top_of_stacks:
    result += t

print(result)