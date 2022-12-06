import os
dir = os.path.dirname(__file__)

outcomes = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3,
}

choiceScores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

choiceMap = {
    0: {'A': 3, 'B': 1, 'C': 2}, # lose
    3: {'A': 1, 'B': 2, 'C': 3}, # draw
    6: {'A': 2, 'B': 3, 'C': 1}, # win
}

choiceOutcomes = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

with open(dir + '/input.txt', 'r') as f:
    rounds = f.read().split("\n")

def partOne(round):
    if not round: return 0
    opponent, space, me = list(round)
    outcomeScore = outcomes[round]
    choiceScore = choiceScores[me]
    return outcomeScore + choiceScore

def partTwo(round):
    if not round: return 0
    opponent, space, outcome = list(round)
    outcomeScore = choiceOutcomes[outcome]
    myChoiceScore = choiceMap[outcomeScore][opponent]
    return outcomeScore + myChoiceScore



# Part one
print(sum(map(partOne, rounds)))

# Part two
print(sum(map(partTwo, rounds)))
