filename = "data/day3_input1.txt"

with open(filename) as f:
    total_priority = 0
    index = 0
    badges = []
    for index, line in enumerate(f):
        if index % 3 == 0:
            groups = [line.strip()]
        else:
            groups.append(line.strip())
        
        line = line.strip()
        midpoint = int(len(line) / 2)
        common = set(line[0:midpoint]).intersection(line[midpoint:])
        numbers = [
            ord(x) - 96 if x.islower() else ord(x) - 38 for x in common
        ]
        total_priority += sum(numbers)
        
        if index % 3 == 2:
            group_common = set.intersection(*map(set, groups))
            badges.append(list(group_common)[0])

badge_values = [
            ord(x) - 96 if x.islower() else ord(x) - 38 for x in badges
        ]
# Part 1
print(total_priority)
# Part 2
print(sum(badge_values))