import re

def part1(data):
    for i, line in enumerate(data):
        data[i] = re.sub('\D', ' ', line).split()
    
    possibilities = [0, 0, 0, 0, 0]
    
    for i, (time, distance) in enumerate(zip(data[0], data[1])):
        time, distance = int(time), int(distance)
        
        for j in range(time):
            this_distance = (time - j) * j

            if this_distance > distance:
                possibilities[i] += 1
            

    return(possibilities)
                

def part2(data):
    for i, line in enumerate(data):
        data[i] = re.sub('\D', '', line)

    possibilities = 0
    curr_percent = 0

    for j in range(int(data[0])):
        this_distance = (int(data[0]) - j) * j

        if this_distance > int(data[1]):
            possibilities += 1

        if (j / int(data[0])) > curr_percent:
            curr_percent += 1/100
            print(curr_percent)
        
    print(data, possibilities)
    return(possibilities)


if __name__ == '__main__':
    data = ['Time:      7  15   30',
            'Distance:  9  40  200']
    if True:
        with open('data6.txt', 'r') as file:
            data = file.readlines()
    #print(data)
    #print(part1(data))
    print(part2(data))
