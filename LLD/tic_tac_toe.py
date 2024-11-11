from abc import ABC, abstractmethod
import random

class Board:
    def __init__(self):
        self.board = [' '] * 9

    def display(self):
        """
        Display the current game baord
        """
        print(f"\n{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")
    
    def update(self, position, symbol):
        """
        Update the board with the player's symbol at the specified position.
        """
        if self.board[position] == " ":
            self.board[position] = symbol
            return True
        return False

    def is_full(self):
        """
        Check if the board is full.
        """
        return ' ' not in self.board
    
    
    def check_winner(self, symbol):
        """
        Check if the given symbol has won the game.
        """
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]
        for a, b, c in win_combinations:
            if self.board[a] == self.board[b] == self.board[c] == symbol:
                return True
        return False
    
class Player(ABC):
    """
    Abstract base class for a Player.
    """
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        pass


class HumanPlayer(Player):
    """
     Human Player class that interacts with the user to get their move.
    """
    def get_move(self, board):
        while True:
            try:
                move = int(input(f"Player {self.symbol}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid input. Please enter a number between 1 and 9.")
                elif board.board[move] != " ":
                    print("The spot is already taken. Please choose another spot.")
                else:
                    return move
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
            

class AIPlayer(Player):
    """
    AI Player class with a basic strategy (random move).
    """
    def get_move(self, board):
        empty_positions = [i for i, x in enumerate(board.board) if x == " "]
        return self.random.choice(empty_positions)
    
class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player_index = 0

    def switch_turn(self):
        """
        Switch the turn to the next player.
        """
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        """
        Start the game loop.
        """
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"Player {current_player.symbol}'s turn.")
            move = current_player.get_move(self.board)
            if not self.board.update(move, current_player.symbol):
                print("Invalid move. Try again.")
                continue
            if self.board.check_winner(current_player.symbol):
                self.board.display()
                print(f"Player {current_player.symbol} wins!")
                break
            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break
            self.switch_turn()


if __name__ == "__main__":
    player1 = HumanPlayer('X')
    player2 = AIPlayer('O')
    game = Game(player1, player2)
    game.play()