from game import Game
from minimax import Minimax
from alpha_beta import AlphaBeta
from math import floor

f = open('input.txt','r')
boardSize = int(f.readline())
algo = f.readline().rstrip()
originPlayer = f.readline().rstrip()
searchDepth = int(f.readline())
boardValues = [["*" for i in range(boardSize)]for j in range (boardSize)]
originBoardState = [["*" for i in range(boardSize)]for j in range (boardSize)]
game = Game(boardValues, boardSize)

minimax = Minimax(searchDepth, game, originPlayer)
alphabeta = AlphaBeta(searchDepth, game, originPlayer)

# Set boardValues
for i in range(boardSize):
    line = f.readline().rstrip()
    line = line.split(" ")
    for j in range(boardSize):
        boardValues[i][j] = int(line[j])

# Set boardState
for i in range(boardSize):
    line = f.readline().rstrip()
    for j in range(boardSize):
        originBoardState[i][j] = line[j]
f.close()

if algo == "MINIMAX":
    result = minimax.Minimax_Decision(originBoardState)
    f = open("output.txt", "w")
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if result[1] == True:
        actionType = "Stake"
    else:
        actionType = "Raid"
    resultIndex = chars[result[0] % boardSize] + str(int(result[0]/boardSize) + 1)
    f.write(resultIndex+ " " + actionType + "\n")
    for i in range(boardSize):
        f.write("".join(result[2][i])+"\n")
    f.close()

if algo == "ALPHABETA":
    result = alphabeta.ABSearch(originBoardState)
    f = open("output.txt", "w")
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', \
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if result[1] == True:
        actionType = "Stake"
    else:
        actionType = "Raid"
    resultIndex = chars[result[0] % boardSize] + str(int(result[0] / boardSize) + 1)
    f.write(resultIndex + " " + actionType + "\n")
    for i in range(boardSize):
        f.write("".join(result[2][i]) + "\n")
    f.
    f.close()

# print(game.PossibleRaids(originBoardState, 'X'))
# print(game.PossibleStakes(originBoardState))
# print(game.MakeRaid(originBoardState, 'O', 4))
# print(game.Score(originBoardState,'O'))
# print(game.Score(originBoardState, originPlayer))