from searching_framework import *
dir = {"Up 1": (0,+1), "Right 1" : (+1,0),"Up 2": (0,+2), "Right 2" : (+2,0),"Up 3": (0,+3), "Right 3" : (+3,0)}

class Ghost(Problem):
    def __init__(self,initial,walls,size,goal=None):
        super().__init__(initial,goal)
        self.walls = walls
        self.size = size
    def successor(self, state):
        successors = dict()
        ghostPos = state
        for action,(dx,dy) in dir.items():
            nx=ghostPos[0]+dx
            ny=ghostPos[1]+dy
            if not (0<=nx<self.size[0] and 0<=ny<self.size[1]):
                continue
            if (nx,ny) in walls:
                continue
            successors[action] = (nx,ny)
        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state == self.goal
    def h(self, node):
        state = node.state
        return (abs(self.goal[0]-state[0]) + abs(self.goal[1]-state[1]))/3
if __name__ == '__main__':
    n = int(input())
    grid = (n,n)
    nm_walls=int(input())
    walls = []
    for i in range(nm_walls):
        walls.append(tuple(map(int, input().split(","))))
    ghost_pos=(0,0)
    pac_pos=((n-1),(n-1))
    initial_state = (0,0)
    problem = Ghost(initial_state,walls,grid,pac_pos)
    solution = astar_search(problem)
    if solution is None:
        print("No solution")
    else:
        print(solution.solution())
