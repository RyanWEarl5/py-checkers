from square import Square

position_dictionary = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
state_dictionary = {"WHITE":"W","BLACK":"B","EMPTY":" "}

class Board:
    
    def __init__(self):
        self.gameboard = [[Square(i,j) for i in range(8)] for j in range(8)]
        self.turn = "WHITE"
        self.new = ""
        self.old = ""
    
    def changeTurn(self):
        self.turn = [i for i in ["WHITE","BLACK"] if self.turn != i][0]
    
    def setPieces(self):
        """ set the gameboard for the beginning of the game """

        def setSide(start, end, color):
            """ set the pieces of a specific side of the board """
            for row in range(start, end):
                if row % 2 != 0:
                    gamesquare = 0 
                else:
                    gamesquare = 1
                for square in self.gameboard[row]:
                    if gamesquare == 1:
                        square.updateState(color)
                        gamesquare = 0
                    else:
                        gamesquare = 1
        
        setSide(0, 3, "white")
        setSide(-3, 0, "black")
        self.printBoard()
                
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

        print("\n--------------------------------------------------\n")

    def updatePositions(self):
        """ update the position of a moved piece, check for captures """
        new_x, new_y = self.new.xpos, self.new.ypos
        old_x, old_y = self.old.xpos, self.old.ypos
        if new_x - old_x == 2:
            if new_y - old_y == 2:
                check = self.gameboard[new_y-1][new_x-1]
                self.checkCapture(check)
            elif new_y - old_y == -2:
                check = self.gameboard[new_y+1][new_x-1]
                self.checkCapture(check)
        elif new_x - old_x == -2:
            if new_y - old_y == 2:
                check = self.gameboard[new_y-1][new_x+1]
                self.checkCapture(check)
            elif new_y - old_y == -2:
                check = self.gameboard[new_x+1][new_x+1]
                self.checkCapture(check)
        else:
            # update states of old and new squares
            self.updateLocations()

    def checkCapture(self, captured):
        """ verify capture makes sense """
        if captured.state == self.turn:
            print("Error: you can't take your own piece")
        elif captured.state == "EMPTY":
            print("Error: you can't jump an empty space")
        else:
            captured.updateState("EMPTY")
            self.updateLocations()

    def updateLocations(self):
        """ update states of moved squares, change turn """
        self.old.updateState("EMPTY")
        self.new.updateState(self.turn)
        self.changeTurn()

    def parseLocation(self, loc):
        """ parse user input locations """
        try:
            xpos, ypos = position_dictionary[loc[0]], int(loc[1])
        except:
            print("Error: improper location format")
        if ypos > 7:
            print("Error: position out of board range")
        return self.gameboard[ypos][xpos]


    def movePiece(self, old_loc, new_loc):
        """ move a piece on the gameboard """
        # return board squares from input move
        self.old = self.parseLocation(old_loc)
        self.new = self.parseLocation(new_loc)

        # check that old position is valid
        if self.old.state == "EMPTY":
            print("Error: no game piece at chosen location")
        elif self.old.state != self.turn:
            print("Error: that is not your piece!")
        else:
            # check that new position is valid
            if self.new.state != "EMPTY":
                print("Error: cannot move on top of another piece")
            elif (self.new.xpos, self.new.ypos) not in self.old.validMoves():
                print("Error: invalid move")
            else:
                self.updatePositions()

    def checkWin(self):
        """ check to see if either side has won the game """
        def countPieces(color):
            return len([item for sublist in self.gameboard for item in sublist if item.state==color])==0
        if countPieces("WHITE"):
            print("Black wins the game!!!")
            return 1
        elif countPieces("BLACK"):
            print("White wins the game!!!")
            return 0

    def takeInputs(self):
        """ get movement inputs from the user """
        old = str(input("Choose Piece: ")).upper()
        new = str(input("Choose Location: ")).upper()
        return old, new

    def playGame(self):
        """ routine to play the game """
        old_pos, new_pos = self.takeInputs()
        self.movePiece(old_pos, new_pos)
        self.printBoard()
        self.checkWin()

