# `A: rock, B: paper, C: scissors
#  X: rock, Y: paper, Z: scissors`

# scoring: 1 for rock, 2 for paper, 3 for scissors
# 0 for losing, 3 for draw, 6 for winning

from read_file import read_file_lines
file_lines = read_file_lines("./data/day2.txt")


# Puzzle 1
# self plays X, Y, Z
winning_rules = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}

draw_rules = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

move_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

score = 0
for line in file_lines:

    current_game = line
    opponent = current_game[0]
    self = current_game[2]

    # draw
    if (draw_rules[opponent] == self):
        score += 3
    # winning
    elif (winning_rules[opponent] == self):
        score += 6
    # move_score
    score += move_score[self]

print("[Puzzle 1: My score: ] : ", score)


# puzzle 2
# P for paper, S for scissors, R for rock
winning_rules = {
    "A": "P",
    "B": "S",
    "C": "R"
}

losing_rules = {
    "A": "S",
    "B": "R",
    "C": "P"

}

draw_rules = {
    "A": "R",
    "B": "P",
    "C": "S"
}

move_score = {
    "R": 1,
    "P": 2,
    "S": 3
}

game_outcome = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
}

score = 0
for line in file_lines:

    current_game = line
    opponent = current_game[0]
    outcome = current_game[2]
    my_move = ""
    # losing
    if (game_outcome[outcome] == "Lose"):
        my_move = losing_rules[opponent]
    # winning
    elif (game_outcome[outcome] == "Win"):
        my_move = winning_rules[opponent]
        score += 6
    # draw
    elif (game_outcome[outcome] == "Draw"):
        my_move = draw_rules[opponent]
        score += 3

    score += move_score[my_move]

print("[Puzzle 2: My score: ] : ", score)
