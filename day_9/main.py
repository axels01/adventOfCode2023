import re
import time


def part1(line):
    line = line.split()

    # line.reverse() # Reverse allows for solution to part 2
    layers = [[]]

    # Convert values to ints
    while line != []:
        layers[0].append(int(line.pop(0)))

    return findNextNum(newLayer(layers))


# Recursive function, returns the "upside-down" derrivatives "pyramid"
def newLayer(layers):
    if all(val == 0 for val in layers[-1]):
        return layers

    # Adds the next "layer"
    layer = []
    for i in range(len(layers[-1])):
        # Will run as long as we're not looking at the 'last' pair
        if (i + 1) >= len(layers[-1]):
            break
        else:
            # Adds the derrivative to the new layer
            layer.append(layers[-1][i + 1] - layers[-1][i])

    # Returns layers with the new layer
    layers.append(layer)
    return newLayer(layers)


# Recursively finds the next 'future' number, going from the
# lowest layer (all zeros) to the original layer
def findNextNum(layers, newNum=0):
    if len(layers) == 1:
        return newNum

    # Pops the lowest layer to currLayer
    layers.pop()

    return findNextNum(layers, newNum + layers[-1][-1])


if __name__ == '__main__':
    start_time = time.time()
    runningTotal = 0
    if True:
        with open('day_9/data.txt', 'r') as data:
            for line in data:
                runningTotal += part1(line)
    else:
        data = ['0 3 6 9 12 15',
                '1 3 6 10 15 21',
                '10 13 16 21 30 45'
                ]
        for line in data:
            print(part1(line))

    print(f'Time: {time.time() - start_time}, total: {runningTotal}')
