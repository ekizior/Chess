# Module to implement each tile of the chess board.

class Tile:

    # Define a new tile object with default settings
    # 
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.name = str(col) + str(8 - row)
        if row % 2 == 0 and col % 2 == 0:
            self.color = "w"
        else:
            self.color = "b"
        self.piece = None
        self.attacked = False

    # Set the piece of this tile to pc
    def set_piece(self, pc):
        self.piece = pc

    # Get the piece of this tile
    def get_piece(self):
        return self.piece

    def get_color(self):
        return self.color
    
    def get_name(self):
        return self.name
