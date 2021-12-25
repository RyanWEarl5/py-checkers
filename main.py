from board import Board

def main():
    """ Run the game routine """

    checker = Board()
    checker.setPieces()
    game_won = False

    while game_won == False:
        game = checker.playGame()
        if game in [0,1]:
            game_won = True

if __name__ == "__main__":
    main()
