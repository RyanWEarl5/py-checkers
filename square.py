class Square:
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.state = "EMPTY"
        self.piece_type = "STANDARD"
    
    def updateState(self, state):
        """ update the state of the square to white, black, or empty """
        input_state = state.upper()
        valid = ["WHITE","BLACK","EMPTY"]
        if input_state in valid:
            self.state = input_state
        else:
            raise ValueError("Error: square state must be one of %r." % valid)

    def updatePieceType(self, type):
        """ update the piece type of the square to standard or king """
        input_type = type.upper()
        valid = ["STANDARD","KING"]
        if input_type in valid:
            self.piece_type = input_type
        else:
            raise ValueError("Error: square type must be one of %r." % valid)

    def validMoves(self):
        """ return moves from this square that are within the board range """
        x, y = self.xpos, self.ypos
        valid_range = range(8)
        if self.piece_type == "KING":
            all_moves = [(2,-2),(2,2),(-2,-2),(-2,2),(1,1),(-1,1),(-1,-1),(1,-1)]
        elif self.state == "BLACK":
            all_moves = [(2,-2),(-2,-2),(1,-1),(-1,-1)]
        elif self.state == "WHITE":
            all_moves = [(2,2),(-2,2),(1,1),(-1,1)]
        valid_moves = []
        for move in all_moves:
            x_delta, y_delta = move
            x_new, y_new = x + x_delta, y + y_delta
            if (x_new in valid_range) and (y_new in valid_range):
                valid_moves.append((x_new,y_new))
        return valid_moves
