from game import Game
from minimax import Minimax

f = open('input.txt','r')
boardSize = int(f.readline())
algo = f.readline().rstrip()
originPlayer = f.readline().rstrip()
searchDepth = int(f.readline())
boardValues = [["*" for i in range(boardSize)]for j in range (boardSize)]
originBoardState = [["*" for i in range(boardSize)]for j in range (boardSize)]
XState = []
OState = []

game = Game(boardValues, boardSize)
minimax = Minimax(searchDepth, game, originPlayer)

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
        if line[j] == 'X':
            XState.append(i * boardSize + j)
        if line[j] == 'O':
            OState.append(i * boardSize + j)

print(game.PossibleStakes(originBoardState))
print(game.PossibleRaids(originBoardState, 'O'))
#print(game.MakeRaid(originBoardState, 'O', 3))
print(game.MakeStake(originBoardState, 'O', 3))

#print(game.Score(originBoardState, originPlayer))