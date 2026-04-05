from examples.abc.abc import solve

from searching_framework import *
dirs = {"Up":(0,+1), "Down":(0,-1), "Left":(-1,0), "Right 2":(2,0), "Right 3":(3,0)}
class House(Problem):
    def __init__(self,initial, grid_size,walls,goal):
        super().__init__(initial,goal)
        self.grid_size = grid_size
        self.walls = walls
    def successor(self, state):
        successors = dict()
        man_pos = state
        for actions, (dx,dy) in dirs.items():
            nx=man_pos[0]+dx
            ny=man_pos[1]+dy
            if not(0<=nx<self.grid_size and 0<=ny<self.grid_size):
                continue
            if (nx,ny) in self.walls:
                continue
            if actions == "Right 2":
                if (nx-1,ny) not in self.walls :
                    successors[actions] = (nx,ny)
            else:
                successors[actions] = (nx,ny)
        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return state == self.goal
    def h(self, node):
        pos = node.state
        return (abs(pos[0]-self.goal[0]) + abs(pos[1]-self.goal[1]))/3
if __name__ == "__main__":
    n = int(input())
    grid = (n,n)
    nm_walls = int(input())
    walls = []
    for i in range(nm_walls):
        walls.append(tuple(map(int,input().split(","))))

    person_pos=tuple(map(int,input().split(",")))
    goal_pos = tuple(map(int,input().split(",")))
    initial = person_pos
    problem = House(initial, n, walls, goal_pos)
    solution = astar_search(problem)
    if solution is not None:
        print(solution.solution())
    else:
        print("No Solution!")