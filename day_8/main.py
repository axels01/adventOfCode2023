import time
import re

def part1(data):
    steps = []
    for char in re.sub('\n', '', data.pop(0)):
        steps.append(char)

    map = {}
    for line in data:
        line = re.sub('\n', '', line)
        if line != '':
            line = re.sub(r'\W', ' ', line).split()
            print(line)
            map[line[0]] = {'L': line[1], 'R': line[2]}

    stepsTaken = 0
    currNode = 'AAA'

    while currNode != 'ZZZ':
        stepsTaken += 1

        step = steps.pop(0)
        steps.append(step)

        currNode = map[currNode][step]

    return stepsTaken


def takeStep(map, stepsTaken, steps):
    pass



if __name__ == '__main__':
    start_time = time.time()
    if True:
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
