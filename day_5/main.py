import time
import re

def part1(data):
    maps = {}
    seeds = re.sub('seeds: ', '', re.sub('\n', '', data.pop(0))).split()
    seed_to_loc = {}
    data.pop(0)
    curr_map = ''
    
    while len(data) > 0:
        line = re.sub('\n', '', data.pop(0))
        if line == '':
            pass
        elif line[0] not in '1234567890':
            line = re.sub(' map:', '', line)
            maps[line] = []
            curr_map = line
        else:
            maps[curr_map].append(line.split())

    for seed in seeds:
        value = int(seed)
        for map_name in maps.keys():
            for line in maps[map_name]:
                dest_start, src_start, rnge = int(line[0]), int(line[1]), int(line[2])

                if value >= src_start and value <= (src_start + rnge):
                    value = (value - src_start) + dest_start
                    seed_to_loc[seed] = value
                    break


    print(seed_to_loc)
    locs = []
    for value in seed_to_loc.values():
        locs.append(value)
    locs.sort()
    return locs[0]

if __name__ == '__main__':
    start_time = time.time()

    with open('day_5/data.txt', 'r') as data:
        print(f'\nPart 1 returned: {part1(data.readlines())}')
            
    print(f'Time: {str(time.time() - start_time)[:8 ]} seconds')
