import tile
import constants as c

# Module that implements the board functionality.

class Board:

    # Create a default board, which is an 8 x 8 list of lists containing tiles.
    def __init__(self):
        self.board = [[tile() for i in range(c.COLS)] for j in range(c.ROWS)]
        self.size = (c.ROWS, c.COLS)

    # Return the tile at (row, col)
    def get_tile(self, row, col):
        return self.board[row][col]
    
    

