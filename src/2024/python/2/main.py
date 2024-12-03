import os
from typing import List

dir = os.path.dirname(__file__)

with open(dir + "/input.txt", "r") as f:
    input = f.read().split("\n")
    input.pop()

sample_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
    "\n"
)

# input = sample_input


class Report:
    levels: List[int]

    def __init__(self, report: str):
        self.levels = [int(val) for val in report.split(" ")]

    def dampend_is_safe(self):
        if self.is_safe():
            return True

        levels_copy = self.levels.copy()
        for i in range(len(self.levels) - 1):
            levels_copy.pop(i)
            if self.is_safe(levels_copy):
                return True
            levels_copy = self.levels.copy()
        return False

    def is_safe(self, levels=None):
        levels = levels or self.levels
        return self.is_unidirectional(levels) and self.is_gradual(levels)

    def is_unidirectional(self, levels):
        return levels == sorted(levels) or levels == sorted(levels, reverse=True)

    def is_gradual(self, levels):
        for i, level in enumerate(levels):
            if i == len(levels) - 1:
                break
            if level == levels[i + 1]:
                return False
            if abs(level - levels[i + 1]) > 3:
                return False
        return True


reports = [Report(line) for line in input]

"""
Part one
"""
# safe_count = 0
# for report in reports:
#     if report.is_safe():
#         safe_count += 1
# print(safe_count)


"""
Part two
"""
safe_count = 0
for report in reports:
    if report.dampend_is_safe():
        safe_count += 1
print(safe_count)
