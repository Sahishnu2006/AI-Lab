        # Base Cases: Evaluate terminal states
        if self.check_winner(board, self.ai):
            return {'position': None, 'score': 10 - depth}
        elif self.check_winner(board, self.human):
            return {'position': None, 'score': depth - 10}
        elif not self.empty_squares():
            return {'position': None, 'score': 0}

        if is_maximizing:
            best = {'position': None, 'score': -math.inf}
            for possible_move in self.available_moves():
                # Make move
                board[possible_move] = self.ai
                # Recurse
                sim_score = self.minimax(board, depth + 1, False)
                # Undo move
                board[possible_move] = ' '
                sim_score['position'] = possible_move

                if sim_score['score'] > best['score']:
                    best = sim_score
            return best
        else:
            best = {'position': None, 'score': math.inf}
            for possible_move in self.available_moves():
                # Make move
                board[possible_move] = self.human
                # Recurse
                sim_score = self.minimax(board, depth + 1, True)
                # Undo move
                board[possible_move] = ' '
                sim_score['position'] = possible_move

                if sim_score['score'] < best['score']:
                    best = sim_score
            return best

    def play(self):
        """Main game loop."""
        print("--- Welcome to Tic-Tac-Toe AI ---")
        print("Board Index Reference:")
        print(" 0 | 1 | 2 ")
        print("---|---|---")
        print(" 3 | 4 | 5 ")
        print("---|---|---")
        print(" 6 | 7 | 8 \n")

        # Human plays 'O', AI plays 'X'
        turn = 'O'  # Human goes first

        while self.empty_squares():
            if turn == self.human:
                self.print_board()
                try:
                    move = int(input("Enter your move (0-8): "))
                    if move not in self.available_moves():
                        print("Invalid move. Try again.")
                        continue
                except ValueError:
                    print("Please enter a valid number between 0 and 8.")
                    continue

                self.board[move] = self.human

                if self.check_winner(self.board, self.human):
                    self.print_board()
                    print("Congratulations! You won!")
                    return
                turn = self.ai

            else:
                print("AI is thinking...")
                move = self.minimax(self.board, 0, True)['position']
                self.board[move] = self.ai

                if self.check_winner(self.board, self.ai):
                    self.print_board()
                    print("AI wins! Better luck next time.")
                    return
                turn = self.human

        self.print_board()
        print("It's a draw!")

# Run the game in Colab
if __name__ == '__main__':
    game = TicTacToe()
    game.play()
