# Module to implement each tile of the chess board.

class Tile:

    # Define a new tile object with default settings
    def __init__(self):
        self.piece = None
        self.attacked = False
    
    # Return if this tile is under attack
    def check_attack(self):
        return self.attacked

    # Set the piece of this tile to pc
    def set_piece(self, pc):
        self.piece = pc
    
    # Set the attacked value of this tile to attacked
    def set_attacked(self, atk):
        self.attacked = atk

    # Get the piece of this tile
    def get_piece(self):
        return self.piece

    # Get the attacked status of this file
    def get_attacked(self):
        return self.attacked
