class Square:
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.state = "EMPTY"
        
    def returnState(self):
        return self.state
    
    def updateState(self, state):
        """ update the state of the square to white, black, or empty """
        input_state = state.upper()
        valid = ["WHITE","BLACK","EMPTY"]
        if input_state in valid:
            self.state = input_state
        else:
            raise ValueError("Error: square state must be one of %r." % valid)
    
    def validMoves(self):
        """ return moves from this square that are within the board range """
        x, y = self.xpos, self.ypos
        valid_range = range(7)
        all_moves = [(2,-2),(2,2),(-2,-2),(-2,2),(0,1)]
        valid_moves = []
        for move in all_moves:
            x_delta, y_delta = move
            x_new, y_new = x + x_delta, y + y_delta
            if (x_new in valid_range) and (y_new in valid_range):
                valid_moves.append((x_new,y_new))


