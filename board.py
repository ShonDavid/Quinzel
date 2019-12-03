from players import Players


class Board():
    def __init__(self, name):
        self.boardArray = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.printArray = """
        {0} | {1} | {2}
        --+---+---
        {3} | {4} | {5}
        --+---+---
        {6} | {7} | {8}
        """
        self.name = name

    def nextMove(self, player, number):
        leftPlaceOnBoard = 0
        rightPlaceOnBoard = 0
        if number == '1':
            leftPlaceOnBoard = 2
            rightPlaceOnBoard = 0
        elif number == '2':
            leftPlaceOnBoard = 2
            rightPlaceOnBoard = 1
        elif number == '3':
            leftPlaceOnBoard = 2
            rightPlaceOnBoard = 2
        elif number == '4':
            leftPlaceOnBoard = 1
            rightPlaceOnBoard = 0
        elif number == '5':
            leftPlaceOnBoard = 1
            rightPlaceOnBoard = 1
        elif number == '6':
            leftPlaceOnBoard = 1
            rightPlaceOnBoard = 2
        elif number == '7':
            leftPlaceOnBoard = 0
            rightPlaceOnBoard = 0
        elif number == '8':
            leftPlaceOnBoard = 0
            rightPlaceOnBoard = 1
        elif number == '9':
            leftPlaceOnBoard = 0
            rightPlaceOnBoard = 2

        if self.boardArray[leftPlaceOnBoard][rightPlaceOnBoard] == " ":
            self.boardArray[leftPlaceOnBoard][rightPlaceOnBoard] = player.symbol
            return False
        else:
            print("Try again!\n")
            return True

    def printBoard(self):
        print(self.printArray.format(self.boardArray[0][0], self.boardArray[0][1], self.boardArray[0][2],
                                     self.boardArray[1][0], self.boardArray[1][1], self.boardArray[1][2],
                                     self.boardArray[2][0], self.boardArray[2][1], self.boardArray[2][2]))

    def isWinner(self):
        if ((self.boardArray[0][0] == self.boardArray[0][1] == self.boardArray[0][2] != " ") or  # top row
            # second row
            (self.boardArray[1][0] == self.boardArray[1][1] == self.boardArray[1][2] != " ") or
            # third row
            (self.boardArray[2][0] == self.boardArray[2][1] == self.boardArray[2][2] != " ") or
            # first column
            (self.boardArray[0][0] == self.boardArray[1][0] == self.boardArray[2][0] != " ") or
            # second column
            (self.boardArray[0][1] == self.boardArray[1][1] == self.boardArray[2][1] != " ") or
            # third column
            (self.boardArray[0][2] == self.boardArray[1][2] == self.boardArray[2][2] != " ") or
            # first diagonal
            (self.boardArray[0][0] == self.boardArray[1][1] == self.boardArray[2][2] != " ") or
                (self.boardArray[2][0] == self.boardArray[1][1] == self.boardArray[0][2] != " ")):  # second diagonal
            print("and the winner is:\n")
            return True
        else:
            return False
