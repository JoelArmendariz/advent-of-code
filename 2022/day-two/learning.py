from enum import Enum
from typing import TYPE_CHECKING, Self


class RPS(Enum):
    # value, score, defeats
    rock = 'A', 1, 'scissors'
    paper = 'B', 2, 'rock'
    scissors = 'C', 3, 'paper'

