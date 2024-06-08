import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


# The class 'TicTacToe' represents a game of Tic-Tac-Toe with methods for making moves, checking for a
# winner, and managing the game board.
class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    """ The `make_board` function in Python returns a list of 9 empty spaces.
        return: A list of 9 empty strings is being returned.
        """
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    """ This static method in Python prints out the numbers for each position on a tic-tac-toe board.
        """
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        """
        The function `make_move` updates the game board with a player's move and checks if the move
        results in a winning condition.

        :param square: The `square` parameter in the `make_move` method likely refers to the position on
        the game board where the player wants to place their letter (X or O). It could be represented as
        an integer or a tuple of coordinates depending on how the game board is structured. The `square`
        parameter
        :param letter: The `letter` parameter in the `make_move` method represents the symbol (e.g., 'X'
        or 'O') that the player wants to place on the game board at the specified `square`
        :return: The `make_move` method returns a boolean value - `True` if the move was successfully
        made and `False` if the square is already occupied.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    """
    The `winner` function in the given Python code checks for a winning condition in a Tic-Tac-Toe game
    based on the provided square and letter.
    
    :param square: The `square` parameter in the `winner` function represents the index of the square on
    the tic-tac-toe board where a player has placed their mark (X or O). The squares are numbered from 0
    to 8, starting from the top-left corner and moving left to right,
    :param letter: It seems like you were about to provide some information about the `letter` parameter
    in your `winner` method, but the information is missing. Could you please provide more details or
    let me know if you need help with something specific related to the `letter` parameter?
    :return: The `winner` function is checking for a winning condition in a Tic-Tac-Toe game based on
    the input square and letter. If a winning condition is found in the row, column, or diagonal that
    includes the specified square and letter, the function returns `True`. Otherwise, it returns
    `False`.
    """

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
    """
    The function 'play' takes in a game, X and O players, and plays the game by alternating player moves
    until there is a winner or a tie.

    :param game: The 'game' parameter is an instance of a Tic-Tac-Toe game that the 'play' function will
    operate on
    :param x_player: The 'x_player' parameter in the 'play' function represents the player who will be
    playing as 'X' in the game. This player will make moves on the game board during the gameplay
    :param o_player: The 'o_player' parameter in the 'play' function represents the player who will be
    playing with the 'O' symbol in the game. This player will make moves on the game board based on the
    logic defined in the 'get_move' method of the player class
    :param print_game: The 'print_game' parameter in the 'play' function is a boolean parameter that
    determines whether the game board and moves are printed during the game. If 'print_game' is set to
    'True', the game board and moves will be printed as the game progresses. If set to 'False',,
    defaults to True (optional)
    :return: The function 'play' returns the letter of the player who wins the game ('X' or 'O'). If the
    game ends in a tie, it returns None.
    """

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
