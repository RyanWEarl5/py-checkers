from Square import Square

position_dictionary = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}

class Board:
    
    def __init__(self):
        self.gameboard = [[Square(i,j) for i in range(8)] for j in range(8)]
    
    def setPieces(self):
        for row in range(2):
            for square in self.gameboard[row]:
                square.updateState("white")
        for row in range(-2,0):
            for square in self.gameboard[row]:
                square.updateState("black")
                
    def printBoard(self):
        print("  " + "   ".join(list(position_dictionary.keys())))
        for row in self.gameboard:
            row_print = []
            for square in row:
                row_print.append(square.icon)
                if row.index(square) != 7:
                    row_print.append(r"|")
            print(str(self.gameboard.index(row)) + " " + " ".join(row_print))
            print("  -----------------------------")
