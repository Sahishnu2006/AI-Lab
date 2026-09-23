# Lab Experiment: Minimax Algorithm for Tic-Tac-Toe
import math

# Step 1: Auxiliary Functions
def check_winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[i] == player for i in line) for line in win_states)

def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

# Step 2: Minimax Core Engine
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'): return 10 - depth
    if check_winner(board, 'O'): return depth - 10
    if not available_moves(board): return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(best_score, score)
        return best_score

# Step 3: Best Move Selector for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for move in available_moves(board):
        board[move] = 'X'
        move_val = minimax(board, 0, False)
        board[move] = ' '
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move

# Step 4: Driver / Execution Loop
def print_board(b):
    for i in range(0, 9, 3):
        print(f" {b[i]} | {b[i+1]} | {b[i+2]} ")
        if i < 6: print("---|---|---")
    print()

board = [' '] * 9
print("Initial Board Indexes: 0 to 8")

while available_moves(board) and not check_winner(board, 'X') and not check_winner(board, 'O'):
    print_board(board)
    user_move = int(input("Enter position (0-8): "))
    if board[user_move] != ' ':
        print("Invalid move, try again!")
        continue
    board[user_move] = 'O'
    
    if check_winner(board, 'O') or not available_moves(board):
        break

    ai_move = find_best_move(board)
    board[ai_move] = 'X'

print_board(board)
if check_winner(board, 'X'): print("Result: AI (X) Wins!")
elif check_winner(board, 'O'): print("Result: Human (O) Wins!")
else: print("Result: Draw Game!")
