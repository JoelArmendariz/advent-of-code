import os
dir =  os.path.dirname(__file__)

with open(dir + '/../calories.txt', 'r') as f:
    calories = f.read().split("\n")
    sums = []
    current_sum = 0

    for count in calories:
        if not count:
            sums.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(count)

    print(max(sums))

