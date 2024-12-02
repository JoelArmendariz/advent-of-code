import os

dir = os.path.dirname(__file__)

with open(dir + "/input.txt", "r") as f:
    input = f.read().split("\n")
    input.pop()

sample_input = """3   4
4   3
2   5
1   3
3   9
3   3""".split(
    "\n"
)

# input = sample_input

left = []
right = []

for pair in input:
    left_value, right_value = pair.split("   ")
    left.append(left_value)
    right.append(right_value)

"""
Part 1
"""
# left.sort()
# right.sort()
#
# print(
#     sum(
#         [
#             int(max(right_value, left_value)) - int(min(right_value, left_value))
#             for left_value, right_value in zip(left, right)
#         ]
#     )
# )

"""
Part 2
"""
total = 0
for left_value in left:
    count = 0
    for right_value in right:
        if left_value == right_value:
            count += 1
    total += int(left_value) * count
print(total)
