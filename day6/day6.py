filename = 'data/day6_input1.txt'

with open(filename, 'r') as f:
    data = f.read().replace('\n','')

def find_packet_marker(data, packet_size):

    first = 0
    while True:
        substring = data[first:packet_size+first]
        if len(substring) == len(set(substring)):
            return first + packet_size
        elif len(substring) == 0:
            raise ValueError('No unique packets found')
        else:
            first += 1

# Part 1
print(find_packet_marker(data, 4))
# Part 2
print(find_packet_marker(data, 14))
