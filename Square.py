state_dictionary = {"WHITE":"W","BLACK":"B","EMPTY":" "}

class Square:
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.state = "EMPTY"
        self.icon = " "
        
    def returnState(self):
        print(self.state)
    
    def updateState(self, state):
        """ update the state of the square to white, black, or empty """
        input_state = state.upper()
        valid = ["WHITE","BLACK","EMPTY"]
        if input_state in valid:
            self.state = input_state
            self.icon = state_dictionary[self.state]
        else:
            raise ValueError("Error: square state must be one of %r." % valid)
