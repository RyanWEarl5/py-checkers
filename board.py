from square import Square

position_dictionary = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
state_dictionary = {"WHITE":"W","BLACK":"B","EMPTY":" "}

class Board:
    
    def __init__(self):
        self.gameboard = [[Square(i,j) for i in range(8)] for j in range(8)]
        self.turn = "WHITE"
    
    def changeTurn(self):
        self.turn = [i for i in ["WHITE","BLACK"] if self.turn != i][0]
    
    def setPieces(self):
        """ set the gameboard for the beginning of the game """
        for row in range(2):
            for square in self.gameboard[row]:
                square.updateState("white")
        for row in range(-2,0):
            for square in self.gameboard[row]:
                square.updateState("black")
                
    def printBoard(self):
        """ print the current state of the gameboard """
        print(f"\n          {self.turn}'S MOVE\n")
        print("  " + "   ".join(list(position_dictionary.keys())))
        for row in self.gameboard:
            row_print = []
            for square in row:
                row_print.append(state_dictionary[square.state])
                if row.index(square) != 7:
                    row_print.append(r"|")
            print(str(self.gameboard.index(row)) + " " + " ".join(row_print))
            print("  -----------------------------")

    def movePiece(self, old_loc, new_loc):
        """ move a piece on the gameboard """

        def parseLocation(loc):
            """ parse user input locations """
            try:
                xpos, ypos = position_dictionary[loc[0]], int(loc[1])
            except:
                raise ValueError("Error: improper location format")
            if ypos > 7:
                raise ValueError("Error: position out of board range")
            return self.gameboard[ypos][xpos]

        def updateLocations(new, old):
            """ update states of moved squares, change turn """
            old.updateState("EMPTY")
            new.updateState(self.turn)
            self.changeTurn()

        def checkCapture(captured):
            """ verify capture makes sense """
            if captured.returnState() == self.turn:
                raise ValueError("Error: you can't take your own piece")
            elif captured.returnState() == "EMPTY":
                raise ValueError("Error: you can't jump an empty space")
            else:
                updateLocations(new_pos, old_piece)


        # return board squares from input move
        old_piece = parseLocation(old_loc)
        new_pos = parseLocation(new_loc)

        # check that old position is valid
        if old_piece.returnState() == "EMPTY":
            raise ValueError("Error: no game piece at chosen location")
        elif old_piece.returnState() != self.turn:
            raise ValueError("Error: that is not your piece!")
        else:
            # check that new position is valid
            print((new_pos.xpos, new_pos.ypos), old_piece.validMoves())
            if new_pos.returnState() != "EMPTY":
                raise ValueError("Error: cannot move on top of another piece")
            elif (new_pos.xpos, new_pos.ypos) not in old_piece.validMoves():
                raise ValueError("Error: invalid move")
            else:
                # check if a piece has been taken
                new_x, new_y = new_pos.xpos, new_pos.ypos
                old_x, old_y = old_piece.xpos, old_piece.ypos
                if new_x != old_x:
                    if new_x > old_x:
                        if new_y > old_y:
                            check = self.gameboard[new_x-1][new_y-1]
                            checkCapture(check)
                        else:
                            check = self.gameboard[new_x-1][new_y+1]
                            checkCapture(check)
                    else:
                        if new_y > old_y:
                            check = self.gameboard[new_x+1][new_y-1]
                            checkCapture(check)
                        else:
                            check = self.gameboard[new_x+1][new_y+1]
                            checkCapture(check)
                else:
                    # update states of old and new squares
                    updateLocations(new_pos, old_piece)
                    
checker = Board()
checker.setPieces()
checker.printBoard()
checker.movePiece("A1","A2")
