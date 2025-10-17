from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[3,1]):
        moves = []
        for row in range(len(board)):
            for count in range(1, board[row]+1):
                moves.append((row, count))
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)
        
    

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves
    

    def result(self, state, move):
        """Return the resulting state after making a move."""
        if move not in state.moves:
            return state
        
        board = state.board[:] # copy of board
        row, count = move
        board[row] -= count

        moves = []
        for r in range(len(board)):
            for c in range(1, board[r]+1):
                moves.append((r, c))

        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        return GameState(to_move=next_player, utility=0, board=board, moves=moves)
    

    def utility(self, state, player):
        """Return 1 if 'player' has won, -1 if 'player' has lost, 0 otherwise."""
        if self.terminal_test(state):
            # If the game ended and it's MAX's turn, MIN made the last move (so MIN won)
            return -1 if state.to_move == 'MAX' else 1
        else:
            return 0

    

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return all(x == 0 for x in state.board)
    

    def display(self, state):
        board = state.board
        print("board: ", board)



if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance

    #nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search

    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2,1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first

    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
