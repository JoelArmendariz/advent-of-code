import os
dir = os.path.dirname(__file__)

with open(dir + '/input.txt', 'r') as f:
    buffer = f.read()

def get_first_marker(marker_size: int) -> None:
    left = 0
    right = marker_size

    while right < len(buffer):
        if len(set(buffer[left:right])) == marker_size:
            print(right)
            break
        left += 1
        right += 1

# part one
get_first_marker(4)

# part two
get_first_marker(14)

