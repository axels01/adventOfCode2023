import re


def part1(lines):
    sum = 0
    already_read = 0

    for index, char in enumerate(lines[1]):
        if already_read > 0:
            already_read -= 1

        elif char in '1234567890':
            number = ''
            for nChar in lines[1][index:]:
                if nChar not in '1234567890':
                    break
                else:
                    number += nChar

            already_read = len(number) - 1

            search_area = str(lines[0][index - 1:index + len(number) + 1] +
                              lines[1][index - 1:index + len(number) + 1] +
                              lines[2][index - 1:index + len(number) + 1])
            if re.sub(r'[.]|[0-9]', '', search_area) != '':
                print(f'    {int(number)}')
                sum += int(number)

    print(f'    Sum: {sum}\n')
    return sum


def part2(lines):
    sum = 0

    for index, char in enumerate(lines[1]):
        if char == '*':
            imid_area = [lines[0][index - 3:index + 4],
                         lines[1][index - 3:index + 4],
                         lines[2][index - 3:index + 4]]
            numbers_touching = []

            for line in imid_area:
                matches = [(match.group(), match.start(),
                            match.end()) for match
                           in re.finditer(r'\d+', line)]
                for match in matches:
                    if 2 <= match[1] <= 4 or 3 <= match[2] <= 5:
                        numbers_touching.append(int(match[0]))
            if len(numbers_touching) == 2:
                sum += int(numbers_touching[0])*int(numbers_touching[1])
    return sum


if __name__ == '__main__':
    rolling_score = 0
    data = []
    if True:
        with open('day_3/data.txt', 'r') as file:
            data = file.read()
            data = data.split('\n')
    # Debugging
    else:
        data = [
                '467..114..',  # 1
                '...*......',
                '..35..633.',  # 3
                '......#...',
                '617*......',  # 5
                '.....+.58.',
                '..592.....',  # 7
                '......755.',
                '...$.*....',  # 9
                '.664.598..'
                ]

    for i in range(len(data)):
        if i == 0:
            rolling_score += part2(['', '.' + data[i], '.' + data[i+1]])
        elif i == len(data)-1:
            rolling_score += part2(['.' + data[i-1], '.' + data[i], ''])
        else:
            rolling_score += part2(['.' + data[i-1], '.' + data[i],
                                    '.' + data[i+1]])

    print(f'Result: {rolling_score}')
