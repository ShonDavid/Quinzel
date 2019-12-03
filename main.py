from players import Players
from board import Board

scoreArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
printArray1 = """
{6} | {7} | {8}
--+---+---
{3} | {4} | {5}
--+---+---
{0} | {1} | {2}
"""

print("Hey There! We play here with the keypad. your keypad looks like this:\n")
print(printArray1.format(scoreArray[0][0], scoreArray[0][1], scoreArray[0][2],
                         scoreArray[1][0], scoreArray[1][1], scoreArray[1][2],
                         scoreArray[2][0], scoreArray[2][1], scoreArray[2][2]))

board = Board("game")

while True:
    symbolPlayerOne = '2'
    symbolPlayerOne = raw_input(
        "To start, please select what you want to be, X or O\n")
    print("you chose {}".format(symbolPlayerOne))
    if symbolPlayerOne == 'X' or symbolPlayerOne == 'O':
        break
    print('Try again!\n')
print('great! Lets play!\n')

playerOne = Players(1, symbolPlayerOne)
symbolPlayerTwo = 'O'
playerTwo = Players(2, symbolPlayerTwo)
if symbolPlayerOne == 'O':
    symbolPlayerTwo = 'X'
    playerTwo == Players(2, symbolPlayerTwo)

board.printBoard()

while True:
    nextMoveNumber = raw_input("Player 1 turn\n")
    while(board.nextMove(playerOne, nextMoveNumber)):
        nextMoveNumber = raw_input("Player 1 turn\n")
        pass
    board.printBoard()
    if(board.isWinner()):
        print("PLAYER 1 WINS!\n")
        break

    nextMoveNumber = raw_input("Player 2 turn\n")
    while(board.nextMove(playerTwo, nextMoveNumber)):
        nextMoveNumber = raw_input("Player 2 turn\n")
        pass
    board.printBoard()
    if(board.isWinner()):
        print("PLAYER 2 WINS!\n")
        break
