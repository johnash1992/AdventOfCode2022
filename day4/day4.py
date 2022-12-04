filename = "data/day4_input1.txt"

num_overlaps = 0
additional_overlaps = 0
with open(filename) as f:
    for l in f.readlines():
        assignments = l.strip().split(',')
        elf1 = list(map(int, assignments[0].split('-')))
        elf2 = list(map(int, assignments[1].split('-')))
        
        if ((elf1[0] <= elf2[0]) and (elf1[1]>=elf2[1])) or \
            ((elf2[0] <= elf1[0]) and (elf2[1]>=elf1[1])):
            num_overlaps += 1
        elif ((elf1[0] <= elf2[1]) and (elf1[1] >= elf2[0])) or \
            ((elf2[0] <= elf1[1]) and (elf2[1] >= elf1[0])):
            additional_overlaps += 1

# Part 1
print(num_overlaps)

#Part 2
print(num_overlaps + additional_overlaps)