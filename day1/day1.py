filename = 'data/day1_input1.txt'

count = 0
elves = []
with open(filename) as f:
    for cal in f.readlines():
        if cal.strip():
            count += int(cal.strip())
        else:
            elves.append(count)
            count = 0

# Part 1
print(max(elves))

# Part 2
print(sum(sorted(elves, reverse=True)[0:3]))