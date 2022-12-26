from typing import List
import os

dir = os.path.dirname(__file__)


class AssignmentPair:
    elf1: List[int]
    elf2: List[int]

    def __init__(self, pair: str) -> None:
        elf_range1, elf_range2 = pair.split(",")
        self.elf1 = [int(value) for value in elf_range1.split("-")]
        self.elf2 = [int(value) for value in elf_range2.split("-")]

    @property
    def is_fully_contained(self) -> bool:
        return (self.elf1[0] <= self.elf2[0] and self.elf1[1] >= self.elf2[1]) or (
            self.elf2[0] <= self.elf1[0] and self.elf2[1] >= self.elf1[1]
        )

    @property
    def is_overlapped(self) -> bool:
        return (self.elf1[0] <= self.elf2[1] and self.elf1[1] >= self.elf2[1]) or (
            self.elf1[1] >= self.elf2[0] and self.elf1[1] <= self.elf2[1]
        )


with open(f"{dir}/input.txt", "r") as f:
    pairs = f.read().split("\n")
    pairs.pop()


def part_one():
    count = 0
    for pair in pairs:
        if AssignmentPair(pair).is_fully_contained:
            count += 1
    return count


print(part_one())


def part_two():
    count = 0
    for pair in pairs:
        if AssignmentPair(pair).is_overlapped:
            count += 1
    return count


print(part_two())
