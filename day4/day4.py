import os, sys 
import numpy as np

# Pre-processing
with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    lines = [l.strip().split(' ') for l in file.readlines() if l.strip() != '']
    
bingo_input = [int(b) for b in lines.pop(0)[0].split(',')]
#print(bingo_index)

for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i] if x != '']
    assert(len(lines[i]) == 5)
    # print(lines[i])

def lines_to_boards(lines):
    boards = []
    for i in range(0, len(lines), 5):
        board = np.array(lines[i:i+5])
        boards.append(board)
    return boards

    
boards = lines_to_boards(lines)
boards_state = [np.empty([5,5]) for n in range(len(boards))]

def update_board_state(board, board_state, number):
    board_state[np.where(board == number)] = -1

def check_winner(board_state):
    for x in range(len(board_state)):
        column = board_state[:,x]
        row = board_state[x,:]
        if np.sum(column) == -5 or np.sum(row) == -5:
            return True
    return False

def caclulate_answer(board, board_state, number):
    answer = np.sum(board[np.where(board_state == 0)]) * number
    return answer

winner_nos = set()
winners = []
def update_boards_state(boards, boards_state, number):
    for i in range(len(boards)):
        board = boards[i]
        state = boards_state[i]
        update_board_state(board, state, number)
        if check_winner(state) and (i not in winner_nos):
            winner_nos.add(i)
            winners.append(caclulate_answer(board, state, number))

for call in bingo_input:
    update_boards_state(boards, boards_state, call)

print(winners[0])
print(winners[-1])