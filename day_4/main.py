import time


def part1(line):
    correct_numbers = 0
    line = line.split('|')

    winning_numbers = line[0].split(':')[1].split()
    my_numbers = line[1].split()

    for num in my_numbers:
        if num in winning_numbers:
            correct_numbers += 1

    if correct_numbers == 0:
        return 0
    else:
        return correct_numbers


def part2(my_cards):
    # For every card in my_cards
    for i, card in enumerate(my_cards):
        # For every copy of the card
        for j in range(card[1]):
            my_cards[i + j + 1][0] += (1 * card[0])
    card_count = 0
    for card in my_cards:
        card_count += card[0]

    return card_count


if __name__ == '__main__':
    start_time = time.time()
    runningTotal = 0
    my_cards = []
    if True:
        with open('data.txt', 'r') as data:
            for line in data:
                score = part1(line)
                runningTotal += (2 ** (score))
                my_cards.append([1, score])
    else:
        data = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
                'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
                'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
                'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
                'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
                'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

        for i, line in enumerate(data):
            score = part1(line)
            runningTotal += (2 ** (score))
            my_cards.append([1, score])

    print(f'Result part 1: {runningTotal}')
    print(f'Result part 2: {part2(my_cards)}')
    print(f'Time: {time.time() - start_time}')
