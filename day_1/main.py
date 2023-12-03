import re


def part1(line):
    line = re.sub('[a-zA-Z]', '', line)
    return (int(line[0] + line[-1]))


def spelled_out_to_digit(numbers, line):
    # Function to remove the first occuranece
    # of substring in string
    result = {}
    keys = []
    for digit, number in enumerate(numbers):
        if line.find(number) >= 0:
            result[line.find(number)] = [number, digit + 1]
            keys.append(line.find(number))

    if keys != []:
        return (line[:min(keys)] +
                str(result[min(keys)][1]) +
                line[int(min(keys) +
                         len(result[min(keys)][0])):])
    else:
        return (line)


def part2(line):
    # Run list as is through function
    numbers = ['one', 'two', 'three',
               'four', 'five', 'six',
               'seven', 'eight', 'nine']
    line = spelled_out_to_digit(numbers, line)

    # Run list and numbers reversed through
    # the same function
    numbers = [i[::-1] for i in numbers]
    line = spelled_out_to_digit(numbers, line[::-1])

    # Runs the once-over reversed line
    # through part1 for the last processing step
    return (part1(line[::-1]))


if __name__ == '__main__':
    rollingScore = 0
    if True:
        with open('day_1/data.txt', 'r') as file:
            for line in file:
                rollingScore += part1(line.replace('\n', ''))
    # Debugging
    else:
        lines = ['twofive2fourfive1dvnrrvjr',
                 'twoeightnq6ninepxv',
                 '39sixgphfvninexts71five',
                 'seven3two8']
        for line in lines:
            print(part2(line))
    print(rollingScore)
