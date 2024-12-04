import os

dir = os.path.dirname(__file__)

with open(dir + "/input.txt", "r") as f:
    input = f.read().split("\n")
    input.pop()

sample_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split(
    "\n"
)

# input = sample_input


"""
Part one
"""
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    # ignore (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def get_directional_substrings(x, y, target_len=3):
    substrings = []
    for direction in directions:
        x_mod, y_mod = direction
        substring = ""
        while len(substring) < target_len:
            if x + x_mod < 0 or x + x_mod > len(input) - 1 or y + y_mod < 0 or y + y_mod > len(input[x + x_mod]):
                break
            try:
                substring += input[x + x_mod][y + y_mod]
            except:
                break
            x_mod += direction[0]
            y_mod += direction[1]
        if len(substring) == target_len:
            substrings.append(input[x][y] + substring)
    return substrings


xmas_count = 0
for x, row in enumerate(input):
    for y, char in enumerate(row):
        directional_substrings = get_directional_substrings(x, y)
        for substring in directional_substrings:
            if substring == "XMAS":
                xmas_count += 1
print(xmas_count)

"""
Part two
"""
corner_mods = [
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
]


def is_mas_cross(x, y):
    if input[x][y] != "A" or x == 0 or x == len(input) - 1 or y == 0 or y == len(input[x]) - 1:
        return False
    top_left = input[x - 1][y - 1]
    top_right = input[x - 1][y + 1]
    bottom_left = input[x + 1][y - 1]
    bottom_right = input[x + 1][y + 1]
    if top_left == "M" and bottom_right == "S" and top_right == "M" and bottom_left == "S":
        return True
    if top_left == "S" and bottom_right == "M" and top_right == "S" and bottom_left == "M":
        return True
    if top_left == "M" and bottom_right == "S" and top_right == "S" and bottom_left == "M":
        return True
    if top_left == "S" and bottom_right == "M" and top_right == "M" and bottom_left == "S":
        return True
    return False


cross_count = 0
for x, row in enumerate(input):
    for y, char in enumerate(row):
        if is_mas_cross(x, y):
            cross_count += 1
print(cross_count)
