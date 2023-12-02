def part1(line):
    # Creates game and line variables by
    # splitting the incomming line by ':', also does
    # some processing for further splitting by ';' and
    # removing the 'Game' from the 'Game #'-substring
    game, line = int(line.split(':')[0][5:]), line.split(':')[1].split(';')

    for roll in line:
        roll = roll.split(',')
        for color in roll:
            if 'red' in color:
                if int(color[1:][:-4]) > 12:
                    return 0
            elif 'green' in color:
                if int(color[1:][:-6]) > 13:
                    return 0
            elif 'blue' in color:
                if int(color[1:][:-5]) > 14:
                    return 0
    return (game)


def part2(line):
    # Remove the 'Game #:' part and splits the
    # resulting line by ';'
    line = line.split(':')[1].split(';')

    red, green, blue = 0, 0, 0

    for roll in line:
        roll = roll.split(',')
        for color in roll:
            if 'red' in color:
                if int(color[1:][:-4]) > red:
                    red = int(color[1:][:-4])
            elif 'green' in color:
                if int(color[1:][:-6]) > green:
                    green = int(color[1:][:-6])
            elif 'blue' in color:
                if int(color[1:][:-5]) > blue:
                    blue = int(color[1:][:-5])

    return (red * green * blue)


if __name__ == '__main__':
    runningTotal = 0
    if True:
        with open('day_2/data.txt', 'r') as data:
            for line in data:
                runningTotal += part2(line)
    # Debugging
    else:
        data = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
        for line in data:
            runningTotal += part1(line)

    print(f'Result: {runningTotal}')
