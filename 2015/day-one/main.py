import os
dir = os.path.dirname(__file__)

with open(dir + '/input.txt', 'r') as f:
    directions = f.read()
    print(directions)

    floor = 0
    direction_num = 0

    for direction in directions:
        if direction == '(':
            floor += 1
            direction_num += 1

        if direction == ')':
            floor -= 1
            direction_num += 1

        if floor < 0:
            break

    print(direction_num)

