class Minimax():
    def __init__(self, searchDepth, game, originPlayer):
        self.searchDepth = searchDepth
        self.log = str()
        self.game = game
        self.originPlayer = originPlayer

    #Return an action
    def Minimax_Decision(self, player, boardState):
        game = self.game
        v = -1e500
        possibleStakes = game.PossibleStakes(boardState)
        possibleRaids = game.PossibleRaids(boardState, player)
        action = possibleStakes.pop()
        stake = True
        resultBoard = boardState
        for a in possibleStakes:
            stakedBoard = game.MakeStake(boardState, player, a)
            score = self.Min_Value(stakedBoard, player, 1)
            if score > v:
                v = score
                action = a
                stake = True
                resultBoard = stakedBoard
        for a in possibleRaids:
            raidedBoard = game.MakeRaid(boardState, player, a)
            score = self.Min_Value(raidedBoard, player, 1)
            if score > v:
                v = score
                action = a
                stake = False
                resultBoard = raidedBoard
        return [action, stake, resultBoard]

    def Max_Value(self, boardState, player, depth):
        game = self.game
        if game.Terminal_Test(boardState):
            return game.Score(boardState, player)
        if depth > self.searchDepth:
            return game.Score(boardState, player)
        v = -1e500
        for a in game.PossibleStakes(boardState):
            v = max(v, self.Min_Value(game.MakeStake(boardState, player, a), game.Oppo(player), depth + 1))
        for a in game.PossibleRaids(boardState, player):
            v = max(v, self.Min_Value(game.MakeRaid(boardState, player, a), game.Oppo(player), depth + 1))
        return v

    def Min_Value(self, boardState, player, depth):
        game = self.game
        if game.Terminal_Test(boardState):
            return game.Score(boardState, player)
        if depth >= self.searchDepth:
            return game.Score(boardState, player)
        v = 1e500
        for a in game.PossibleStakes(boardState):
            v = min(v, self.Max_Value(game.MakeStake(boardState, player, a), game.Oppo(player), depth + 1))
        for a in game.PossibleRaids(boardState, player):
            v = min(v, self.Max_Value(game.MakeRaid(boardState, player, a), game.Oppo(player), depth + 1))
        return v
