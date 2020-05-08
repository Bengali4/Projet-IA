from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax, TT
import pprint

class Avalam(TwoPlayersGame):
    def __init__(self, players, grid, tower):
        self.players = players
        self.grid = grid
        self.nplayer = 1
        self.tower = tower
        self.directions = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
    def possible_moves(self):
        movelist = []
        for l, line in enumerate(self.grid):
            for c, case in enumerate(line):
                if len(case) >= 1 and len(case) <= 4:
                    for direction in self.directions:
                        nextl= l + direction[0]
                        nextc = c + direction[1]
                        if nextl in range(0, 9) and nextc in range(0, 9):
                            if len(self.grid[nextl][nextc]) != 0 and len(self.grid[l][c])+len(self.grid[nextl][nextc]) <= 5:
                                movelist.append([[l, c], [nextl, nextc]])
        return movelist
    def make_move(self,move):
        self.grid[move[1][0]][move[1][1]][:] = self.grid[move[1][0]][move[1][1]] + self.grid[move[0][0]][move[0][1]]
        self.grid[move[0][0]][move[0][1]][:] = []
    def scoring(self):
        tower0 = 0
        tower1 = 0
        score = 0
        for l, line in enumerate(self.grid):
            for c, case in enumerate(line):
                if len(case) in range(1, 6):
                    if case[len(case)-1] == 0 :
                        tower0 += 1
                        if len(case) == 5:
                            tower0 += 2
                    else:
                        tower1 += 1
                        if len(case) == 5:
                            tower1 += 2
        if self.nplayer == 1:
            if self.tower == 0:
                score = (tower0 - tower1)
            else:
                score = (tower1 - tower0)
        else:
            if self.tower == 0:
                score = (tower1 - tower0)
            else:
                score = (tower0 - tower1)
        # print("nouvelle feuille")
        # print(self.nplayer)
        # print(score)
        # self.show()
        return score
    def is_over(self):
        for l, line in enumerate(self.grid):
            for c, case in enumerate(line):
                if len(case) >= 1 and len(case) <= 4:
                    for direction in self.directions:
                        nextl= l + direction[0]
                        nextc = c + direction[1]
                        if nextl in range(0, 9) and nextc in range(0, 9):
                            if len(self.grid[nextl][nextc]) != 0 and len(self.grid[l][c])+len(self.grid[nextl][nextc]) <= 5:
                                return False
        return True
    def show(self):
        pprint.pprint(self.grid)

def aieasyup(body):
    grid = body["game"]
    tower = body["players"].index(body["you"])
    depth = 2
    if len(body["moves"]) > 24:
        depth = (len(body["moves"]) // 8)
    print(depth)
    ai = Negamax(depth)
    game = Avalam([AI_Player(ai), Human_Player()], grid, tower)
    ai_move = game.get_move()
    move = {"from": ai_move[0], "to": ai_move[1]}
    return {"move": move}

# grid2 = [[[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [1, 1, 0, 0, 1], [], [], [], []], [[], [], [], [], [0], [], [0, 0, 1, 1], [], [0, 0, 0, 1, 1]], [[], [], [1, 1, 1, 0, 0], [], [], [], [1, 1, 0, 1, 0], [], []], [[], [], [0], [1, 0], [0], [1], [], [], []], [[1], [0], [1, 1, 0, 0], [0], [1], [0], [1, 0], [], []], [[], [1], [0], [1], [0], [1], [], [], []], [[], [], [], [], [1], [0], [], [], []]]
# grid0 = [
# 		[ [],  [],  [], [], [],  [],  [],  [],  []],
# 		[ [],  [],  [], [], [], [], [], [],  []],
# 		[ [],  [], [], [0, 1], [], [], [], [], []],
# 		[ [],  [], [], [1,0,1], [0,1,0], [], [], [], []],
# 		[ [], [], [], [],  [], [], [], [],  []],
# 		[ [1], [1], [], [1], [], [1,1,0,0,1], [],  [],  []],
# 		[ [0], [], [], [], [0], [], [],  [],  []],
# 		[ [], [], [], [], [], [],  [],  [],  []],
# 		[ [],  [],  [],  [], [], [],  [],  [],  []]
# 	]
# ai = Negamax(3)
# game = Avalam([AI_Player(ai), Human_Player()], grid0, 1)
# # score = game.scoring()
# # print(score)
# # print(game.make_move([[3, 4], [2, 3]]))
# # print(game.show())
# ai_move = game.get_move()
# print(ai_move)
# game.play()