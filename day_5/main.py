import time
import re
import math

def part1(data):
    start_time = time.time()
    maps = {}
    seeds = re.sub('seeds: ', '', re.sub('\n', '', data.pop(0))).split()
    seed_to_loc = {}
    curr_low = 10000000000
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

    total_nums = 0
    curr_percent = 0.0001
    curr_num = 0
    seed_pairs = list(zip(seeds[::2], seeds[1::2]))
         
    for pair in seed_pairs:
        total_nums += (int(pair[1]))
    
    #print(total_nums)
    
    for pair in seed_pairs:
        for seed in range(int(pair[0]), int(pair[0]) + int(pair[1])):
            #print(seed)
            curr_num += 1
            if (curr_num / total_nums) >= curr_percent:
                print(f'{str(curr_percent)[2:]}% at {str(time.time() - start_time)[:8 ]} seconds')
                curr_percent += 0.0001

            value = int(seed)
            for map_name in maps.keys():
                for line in maps[map_name]:
                    dest_start, src_start, rnge = int(line[0]), int(line[1]), int(line[2])

                    if value >= src_start and value <= (src_start + rnge):
                        value = (value - src_start) + dest_start
                        if value < curr_low:
                            print(f'New low: {value}')
                            curr_low = value
                            break
                        break


    # print(seed_to_loc)
    # locs = []
    # for value in seed_to_loc.values():
    #     locs.append(value)
    # locs.sort()
    return curr_low

if __name__ == '__main__':
    start_time = time.time()

    with open('data.txt', 'r') as data:
        print(f'\nPart 1 returned: {part1(data.readlines())}')
            
    print(f'Time: {str(time.time() - start_time)[:8 ]} seconds')
