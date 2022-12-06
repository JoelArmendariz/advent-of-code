import os
dir = os.path.dirname(__file__)


with open(dir + '/input.txt', 'r') as f: 
    input = f.read().split("\n")
    input.pop()

def strip_col(col):
    return col.replace('[', ' ').replace(']', ' ')

stripped_stacks = map(strip_col, input[:8])
stacks_input = [list(stack) for stack in zip(*stripped_stacks) if stack[-1] != ' ']


class Stack:
    def __init__(self, stack):
        copy = stack[:]
        copy.reverse()
        self.crates = [crate for crate in copy if crate != ' ']

    def add_crate(self, crate):
        self.crates.append(crate)

    def take_crate(self):
        return self.crates.pop()

    def get_top_crate(self):
        if len(self.crates) == 0:
            return ' '
        return self.crates[-1]


class Directions:
    def __init__(self, directions):
        _move, count, _from, source, _to, destination = directions.split(' ')
        self.count = int(count)
        self.source = int(source) - 1
        self.destination = int(destination) - 1


stacks = [Stack(stack) for stack in stacks_input]
directions = [Directions(direction) for direction in input[10:]]
 
 
# part one
for direction in directions:
    source = stacks[direction.source]
    destination = stacks[direction.destination]
    crates_to_move = []
    for _ in range(direction.count):
        crates_to_move.append(source.take_crate())

    for crate in crates_to_move:
        destination.add_crate(crate)

print([stack.get_top_crate() for stack in stacks])


# part two
for direction in directions:
    source = stacks[direction.source]
    destination = stacks[direction.destination]
    crates_to_move = []
    for _ in range(direction.count):
        crates_to_move.insert(0, source.take_crate())

    for crate in crates_to_move:
        destination.add_crate(crate)

print([stack.get_top_crate() for stack in stacks])

