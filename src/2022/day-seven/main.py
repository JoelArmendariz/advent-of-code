from __future__ import annotations
from typing import List, Optional
import os
dir = os.path.dirname(__file__)

with open(f'{dir}/input.txt', 'r') as f:
    history = f.read().split('\n')
    history.pop()

class Node:
    def __init__(self, name: str, parent: Optional[Node]) -> None:
        self.name: str = name
        self.parent: str = parent
        self.files: List[tuple[str, int]] = []
        self.directories: dict[str, Node] = {}

    def get_size(self) -> int:
        return sum(map(lambda file: file[1], self.files)) \
            + sum(map(lambda directory: directory.get_size(), self.directories.values()))


def build_file_system(entries: List[str]) -> Node:
    root_node = current_node = Node('/', None)

    for entry in entries:
        match entry.split(' '):
            case ['$', 'cd', '/']:
                current_node = root_node
            case ['$', 'cd', '..']:
                current_node = current_node.parent
            case ['$', 'cd', directory_name]:
                current_node = current_node.directories[directory_name]
            case ['dir', directory_name]:
                current_node.directories[directory_name] = Node(directory_name, current_node)
            case ['$', 'ls']:
                continue
            case [file_size_str, file_name]:
                current_node.files.append([file_name, int(file_size_str)])

    return root_node


def part_one():
    system = build_file_system(history)
    sum = 0

    directories = [system]
    while len(directories) > 0:
        current_directory = directories.pop()
        directory_size = current_directory.get_size()
        if directory_size < 100000:
            sum += directory_size
        directories.extend(current_directory.directories.values())

    return sum

print(part_one())


def part_two():
    system = build_file_system(history)
    file_system_disk_space = 70000000
    free_space = file_system_disk_space - system.get_size()
    target_free_space = 30000000

    eligible_directories = []

    directories = [system]
    while len(directories) > 0:
        current_directory = directories.pop()
        directory_size = current_directory.get_size()
        if free_space + directory_size >= target_free_space:
            eligible_directories.append(directory_size)
        directories.extend(current_directory.directories.values())

    return min(eligible_directories)

print(part_two())
