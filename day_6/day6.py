import re


def part1(data):
    # Cleans input data
    for i, line in enumerate(data):
        data[i] = re.sub('\D', ' ', line).split()
    possibilities = [0, 0, 0, 0, 0]

    # For every pair of time and record distance
    for i, (time, distance) in enumerate(zip(data[0], data[1])):
        time, distance = int(time), int(distance)
        # Check every possibility of time spent on the button
        for j in range(time):
            this_distance = (time - j) * j
            # Checks whether the distance is greater
            if this_distance > distance:
                possibilities[i] += 1

    return possibilities


def part2(data):
    for i, line in enumerate(data):
        data[i] = re.sub('\D', '', line)

    possibilities = 0
    curr_percent = 0

    # Very similar to the above inner for-loop
    # Checks every possibility and calculates distance
    for j in range(int(data[0])):
        this_distance = (int(data[0]) - j) * j

        # When the distance is better than the current record
        if this_distance > int(data[1]):
            possibilities += 1
        # Used to check how far through the list we've gotten
        if (j / int(data[0])) > curr_percent:
            curr_percent += 1/100
            print(str(curr_percent)[2:4] + '%')

    print(data, possibilities)
    return possibilities


if __name__ == '__main__':
    data = ['Time:      7  15   30',
            'Distance:  9  40  200']

    if True:
        with open('day_6/data.txt', 'r') as file:
            data = file.readlines()

    # print(part1(data))
    print(part2(data))
