from math import floor
from copy import deepcopy

class Game:
    def __init__(self, boardValues, boardSize):
        self.boardValues = boardValues
        self.boardSize = boardSize
        self.tuple_in_dir = lambda tuple1, direction: (tuple1[0] + direction[0], tuple1[1] + direction[1])
        self.tuple_valid = lambda tuple1: (tuple1[0] >= 0 and tuple1[0] < boardSize and tuple1[1] >= 0 \
                                           and tuple1[1] < boardSize)
        self.index = lambda n: (int(floor(n / boardSize)), int((n) % boardSize))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def Terminal_Test(self, boardState):
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if boardState[i][j] == ".":
                    return False
        return True

    #return score based on boardState
    def Score(self, boardState, player):
        playerScore = 0
        oppoScore = 0
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if boardState[i][j] == player:
                    playerScore += self.boardValues[i][j]
                elif boardState[i][j] == self.Oppo(player):
                    oppoScore += self.boardValues[i][j]
        return playerScore - oppoScore

    #return a set of all the possible stake
    def PossibleStakes(self, boardState):
        possibleStakes = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if boardState[i][j] == '.':
                    possibleStakes.append(i * self.boardSize + j)
        return possibleStakes

    #return a set of all the possible moves
    def PossibleRaids(self, boardState, player):
        possibleRaids = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if boardState[i][j] != ".":
                    continue
                hasPlayerNeighbour = False
                hasOppoNeighbour = False
                for direction in self.directions:
                    t = self.tuple_in_dir((i, j), direction)
                    if self.tuple_valid(t) and boardState[t[0]][t[1]] == player:
                        hasPlayerNeighbour = True
                    if self.tuple_valid(t) and boardState[t[0]][t[1]] == self.Oppo(player):
                        hasOppoNeighbour = True
                if hasPlayerNeighbour and hasOppoNeighbour:
                    possibleRaids.append(i * self.boardSize + j)
        return possibleRaids

    #operate a raid and return the state
    def MakeRaid(self, boardState, player, move):
        changedState = deepcopy(boardState)
        indexTuple = self.index(move)
        changedState[indexTuple[0]][indexTuple[1]] = player
        for direction in self.directions:
            t = self.tuple_in_dir((indexTuple[0], indexTuple[1]), direction)
            if self.tuple_valid(t) and changedState[t[0]][t[1]] == self.Oppo(player):
                changedState[t[0]][t[1]] = player
        return changedState

    #operate a stake and return the state
    def MakeStake(self, boardState, player, move):
        changedState = deepcopy(boardState)
        indexTuple = self.index(move)
        changedState[indexTuple[0]][indexTuple[1]] = player
        return  changedState

    def Oppo(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'