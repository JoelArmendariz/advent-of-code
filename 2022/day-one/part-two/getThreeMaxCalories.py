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

    largest_sum = max(sums)
    largest_three = [largest_sum]
    current_largest = 0

    while (len(largest_three) < 3):
        for sum in sums:
            if sum > current_largest and sum < largest_three[len(largest_three) - 1]:
                current_largest = sum
        largest_three.append(current_largest)
        current_largest = 0

    print(largest_three[0] + largest_three[1] + largest_three[2])
