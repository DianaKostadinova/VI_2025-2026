from searching_framework import *
dir = {"up":(0,+1), "down":(0,-1),"right":(1,0), "up-right":(+1,+1),  "down-right":(1,-1) }
cant_use = [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4) ,(4,5),(5,3),(5,4),(5,5),(6,3),(6,4),(6,5)]
class Football(Problem):
    def __init__(self,initial, player1, player2, goal=None):
        self.initial = initial
        self.player1 = player1
        self.player2 = player2
        self.goal = goal
    def successor(self, state):
        successors = dict()
        personPos, ballPos = state
        for actions, (dx,dy) in dir.items():
            nx = personPos[0]+dx
            ny = personPos[1]+dy
            newBall=ballPos
            if not (0<=nx<8 and 0<=ny<6):
                continue
            if (nx,ny) == self.player1 or (nx,ny) == self.player2:
                continue
            if (nx, ny) == ballPos:
                newBall = (ballPos[0]+dx, ballPos[1]+dy)
                if newBall not in cant_use and 0<=newBall[0]<8 and 0<=newBall[1]<6:
                    successors[f"Push ball {actions}"] = (nx, ny), newBall
                else :
                    continue
            else:
                successors[f"Move man {actions}"] = (nx, ny), newBall


        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state,action):
        return self.successor(state)[action]
    def goal_test(self, state):
        _,ball_pos = state
        return ball_pos in self.goal
if __name__ == "__main__":
    grid =(8,6)
    goalPos = [(7,2),(7,3)]
    opps = [(3,3), (4,5)]
    player = tuple(map(int, input().split(",")))
    ball_pos = tuple(map(int, input().split(",")))
    initial = player,ball_pos
    problem = Football(initial, opps[0],opps[1], goalPos)
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())