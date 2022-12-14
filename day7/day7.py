filename = 'data/day7_input1.txt'

with open(filename, 'r') as f:
    file_structure = {}
    for line in f.readlines():
        line = line.strip()
        if line[0:4] == '$ cd':
            change_to = line.split()[2]
            if change_to == '/':
                current_path = []
            elif change_to == '..':
                current_path = current_path[0:-1]
            else:
                current_path.append(change_to)
            path_string = '/' + '/'.join(current_path)
            if path_string not in file_structure:
                file_structure[path_string] = 0
            
        elif line.split()[0].isnumeric():
            file_structure[path_string] += int(line.split()[0])

dir_sizes = []
for key in file_structure:

    total_size = sum([v for k, v in file_structure.items() if k.startswith(key)])
    dir_sizes.append(total_size)

# Part 1
print(sum([x for x in dir_sizes if x < 100000]))


# Part 2
disk_space = 70000000
req_space = 30000000
used_space = dir_sizes[0]
extra_space_needed =  req_space + used_space - disk_space
print(min([x for x in dir_sizes if x > extra_space_needed]))