GAME_POINTS = {
    'ROCK' : {'VALUE':1, 'ROCK':3, 'PAPER':0, 'SCISSORS':6},
    'PAPER' : {'VALUE':2, 'ROCK':6, 'PAPER':3, 'SCISSORS':0},
    'SCISSORS' : {'VALUE':3, 'ROCK':0, 'PAPER':6, 'SCISSORS':3}
}

CODE_ABC = {'A':'ROCK', 'B':'PAPER', 'C':'SCISSORS'}
CODE_XYZ = {'X':'ROCK', 'Y':'PAPER', 'Z':'SCISSORS'}

def my_move_score(my_move, their_move):
    game_score = GAME_POINTS[my_move]
    return game_score['VALUE'] + game_score[their_move]

their_moves = {
    'A' : {'X':'Z', 'Y':'X', 'Z':'Y'},
    'B' : {'X':'X', 'Y':'Y', 'Z':'Z'},
    'C' : {'X':'Y', 'Y':'Z', 'Z':'X'},
}

myscore_part1 = 0
myscore_part2 = 0
with open('data/day2_input1.txt') as f:
    for strategy in f.readlines():
        their_move_code, my_move_code = strategy.split()
        their_move = CODE_ABC[their_move_code]
        my_move = CODE_XYZ[my_move_code]
        myscore_part1 += my_move_score(my_move, their_move)

        my_actual_move = CODE_XYZ[their_moves[their_move_code][my_move_code]]
        myscore_part2 += my_move_score(my_actual_move, their_move)


# Part 1
print(myscore_part1)
# Part 2
print(myscore_part2)