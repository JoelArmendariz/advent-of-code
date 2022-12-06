import os
dir = os.path.dirname(__file__)

with open(dir + '/input.txt', 'r') as f:
    rounds = f.read().split("\n")
    rounds.pop()

game_map = {
   'A': ['rock', 1, 'scissors', 'paper'],
   'X': ['rock', 1, 'scissors', 'paper'],
   'B': ['paper', 2, 'rock', 'scissors'],
   'Y': ['paper', 2, 'rock', 'scissors'],
   'C': ['scissors', 3, 'paper', 'rock'],
   'Z': ['scissors', 3, 'paper', 'rock'],
   'rock': 'A',
   'paper': 'B',
   'scissors': 'C',
}

class RPS:
    choice: str
    score: int
    defeats: str
    defeated_by: str

    def __init__(self, choice_key: str) -> None:
        self.choice, self.score, self.defeats, self.defeated_by = game_map[choice_key]

    def __gt__(self, opponent) -> bool:
        return self.defeats == opponent.choice


# part one
def get_round_results(round: str) -> int:
    _opponent, _own = round.split(' ')

    own = RPS(_own)
    opponent = RPS(_opponent)

    round_score = 0

    if own > opponent:
        round_score = 6
    elif own < opponent:
        round_score = 0
    else:
        round_score = 3

    return round_score + own.score

print(sum([get_round_results(round) for round in rounds]))


# part two
def choose_round_outcome(round: str) -> int:
    _opponent, _outcome = round.split(' ')
    
    opponent = RPS(_opponent)

    round_score = 0
    own_score = 0

    if _outcome == 'X':
        own_score = RPS(game_map[opponent.defeats]).score
    elif _outcome == 'Y':
        own_score = RPS(game_map[opponent.choice]).score
        round_score = 3
    else:
        own_score = RPS(game_map[opponent.defeated_by]).score
        round_score = 6
    
    return round_score + own_score

print(sum([choose_round_outcome(round) for round in rounds]))
