import time
import re


def part1(data):
    steps = []
    # Cleans the line
    for char in re.sub('\n', '', data.pop(0)):
        steps.append(char)

    # Creates the map from input data, map consists of
    # dict where the key is the node name and value is
    # a list with its "left" and "right" values in a list
    map = {}
    for line in data:
        line = re.sub('\n', '', line)
        if line != '':
            line = re.sub(r'\W', ' ', line).split()
            map[line[0]] = {'L': line[1], 'R': line[2]}

    # Counter for steps taken (used for final output/result)
    stepsTaken = 0
    # Starting node is always 'AAA'
    currNode = 'AAA'

    # As long as the current node is not 'ZZZ'
    while currNode != 'ZZZ':
        stepsTaken += 1

        # Pops the "next" step (L or R) and appends it to
        # the back of the list since the "path" repeats
        # itself at the end
        step = steps.pop(0)
        steps.append(step)

        # Updates value of current node to the next node
        # based upon step (L or R)
        currNode = map[currNode][step]

    return stepsTaken


if __name__ == '__main__':
    start_time = time.time()
    if True:
        with open('day_8/data.txt', 'r') as data:
            lines = []
            for line in data:
                lines.append(line)
            print(f'\nPart 1 returned: {part1(lines)}')
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

    print(f'Time: {str(time.time() - start_time)[:8 ]} seconds')
