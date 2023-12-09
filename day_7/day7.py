import re
import time

def part1(hand):
    bet = hand.pop()
    hand = hand.pop()



    print(hand)
    print(bet)
    return(getType(hand) * int(bet))

def getType(hand):
    cards = [ 'A ', 'K ', 'Q ', 'J ', 
              'T ', '9 ', '8 ', '7 ', 
              '6 ', '5 ', '4 ', '3 ', '2']
    

    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card, where all cards' labels are distinct: 23456
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
    pass

if __name__ == '__main__':
    start_time = time.time()
    my_cards = []
    if False:
        with open('day_7/data.txt', 'r') as data:
            for line in data:
                part1(line.split())
    else:
        data = ['32T3K 765',
                'T55J5 684',
                'KK677 28',
                'KTJJT 220',
                'QQQJA 483']
        for line in data:
                part1(line.split())

    print(f'Time: {time.time() - start_time}')