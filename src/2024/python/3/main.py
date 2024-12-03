import os
import re

dir = os.path.dirname(__file__)

with open(dir + "/input.txt", "r") as f:
    input = f.read()


def multiply(mul_str: str):
    prefix, suffix = mul_str.split(",")
    num1 = int(prefix[4:])
    num2 = int(suffix[:-1])
    return num1 * num2


"""
Part one
"""
part_one_sample_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
mul_matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input)

# print(sum([multiply(mul_str) for mul_str in mul_matches]))


"""
Part two
"""
part_two_sample_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
do_dont_mul_matches = re.findall(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", input)

sum = 0
do = True
for match in do_dont_mul_matches:
    if match == "don't()":
        do = False
    elif match == "do()":
        do = True
    elif do:
        sum += multiply(match)
print(sum)
