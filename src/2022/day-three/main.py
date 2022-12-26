from typing import List
import string
import os

dir = os.path.dirname(__file__)


class Rucksack:
    items: str
    compartment1: str
    compartment2: str

    def __init__(self, compartments: str) -> None:
        mid_point = len(compartments) // 2
        self.items = compartments
        self.compartment1 = compartments[:mid_point]
        self.compartment2 = compartments[mid_point:]

    @property
    def common_item(self) -> str:
        set1 = set(self.compartment1)
        set2 = set(self.compartment2)
        return list(set1.intersection(set2))[0]


def get_item_priority(s: str) -> int:
    return string.ascii_letters.index(s) + 1


with open(f"{dir}/input.txt", "r") as f:
    rucksacks = f.read().split("\n")
    rucksacks.pop()


def part_one():
    return sum(
        [get_item_priority(Rucksack(rucksack).common_item) for rucksack in rucksacks]
    )


def get_badge_for_group(group: List[Rucksack]) -> str:
    items1, items2, items3 = [rucksack.items for rucksack in group]
    return list(set(items1) & set(items2) & set(items3))[0]


print(part_one())


def part_two():
    it = iter(rucksacks)
    badges = []
    for group in zip(it, it, it):
        badges.append(get_badge_for_group([Rucksack(rucksack) for rucksack in group]))
    return sum([get_item_priority(badge) for badge in badges])


print(part_two())
