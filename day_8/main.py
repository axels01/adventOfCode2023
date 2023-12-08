import time
import re

def part1(data):
    steps = data.pop(0)
    map = {}

    print(f'Steps: {steps}')
    print(f'Map: {data}')

    for line in data:
        line = re.sub(r'\W+', ' ', line).split()
        print(line)
        map[line[0]] = {'L': line[1], 'R': line[2]}




    return map


def takeStep():


if __name__ == '__main__':
    start_time = time.time()
    if False:
        with open('data.txt', 'r') as data:
            print(f'\nPart 1 returned: {part1(data.readlines())}')
    else:
        data = [
            'RL',

            'AAA = (BBB, CCC)',
            'BBB = (DDD, EEE)',
            'CCC = (ZZZ, GGG)',
            'DDD = (DDD, DDD)',
            'EEE = (EEE, EEE)',
            'GGG = (GGG, GGG)',
            'ZZZ = (ZZZ, ZZZ)'
        ]

    print(part1(data))
            
    print(f'Time: {str(time.time() - start_time)[:8 ]} seconds')
