class Minimax():
    def __init__(self, searchDepth, game, originPlayer):
        self.searchDepth = searchDepth
        self.log = str()
        self.game = game
        self.originPlayer = originPlayer

    #Return an action
    def Minimax_Decision(self, player, boardState, possibleActions, gameOperation):
        game = self.game
        v = -1e500
        possibleStakes = game.PossibleStakes(boardState)
        action = possibleStakes[0]
        for a in possibleStakes:
            if game.Score(a) > v:
                v = game.Score(a)
                action = a
        return action

    def Max_Value(self, boardState, player, depth = 1):
        game = self.game
        if game.Terminal_Test(boardState):
            return game.Score(boardState)
        v = -1e500
        for a in game.PossibleStakes(boardState):
            v = max(v, self.Min_Value(game.MakeStake(boardState, player), game.Oppo(player)))
        return v

    def Min_Value(self, boardState, player, depth = 1):
        game = self.game
        if game.Terminal_Test(boardState):
            return game.Score(boardState)
        v = 1e500
        for a in game.PossibleStakes():
            v = min(v, self.Max_Value(game.MakeStake(boardState, player)), game.Oppo(player))
        return v
