import heapq
import os
dir = os.path.dirname(__file__)

with open(dir + '/input.txt', 'r') as f:
    calories = f.read().split("\n")

sum_groups = []
new_group = []

for amount in calories:
    if amount == '':
        sum_groups.append(sum(new_group))
        new_group = []
        continue
    new_group.append(int(amount))

# part one
print(max(sum_groups))

# part two
print(sum(heapq.nlargest(3, sum_groups)))
