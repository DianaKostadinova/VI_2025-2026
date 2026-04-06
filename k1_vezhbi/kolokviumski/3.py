from searching_framework import *
dirs = {"Gore":(0,+1), "Dolu":(0,-1), "Levo":(-1,0), "Desno":(+1,0), "Stoj":(0,0)}
class Maze(Problem):
    def __init__(self,initial,n,m,walls,goal):
        super().__init__(initial,goal)
        self.n = n
        self.m = m
        self.walls = walls
    def successor(self, state):
        successors = dict()
        (x,y), time,laser = state
        for actions, (dx,dy) in dirs.items():
            nx= x+dx
            ny= y+dy
            if (nx, ny) in self.walls:
                continue
            if not (0<=nx<self.n and 0<=ny<self.m):
                continue
            new_laser_pos = laser
            new_time = time +1
            if time == 1:
                new_laser_pos = (nx,ny)
            if time == 4:
                new_time = 1
                if nx == new_laser_pos[0] or ny == new_laser_pos[1]:
                    continue
            successors[actions] = (nx,ny), new_time,new_laser_pos
        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        (x,y), time,laser = state
        return (x,y) == self.goal

if __name__ == '__main__':
    n,m = map(int, input().split())

    start_pos = tuple(map(int,input().split()))
    target_pos = tuple(map(int,input().split()))

    timer = int(input())
    laser = tuple(map(int,input().split()))
    nm_walls = int(input())
    walls = []
    for i in range(nm_walls):
        walls.append(tuple(map(int,input().split())))
    initial = start_pos, timer, laser
    problem = Maze(initial, n,m,walls, target_pos)
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())