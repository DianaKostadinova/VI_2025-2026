from searching_framework import *
dirs = {"Up 1":(0,+1), "Up-right 1":(+1,+1), "Up-left 1":(-1,+1),"Up 2":(0,+2), "Up-right 2":(+2,+2), "Up-left 2":(-2,+2), "Wait":(0,0)}

class House(Problem):
    def __init__(self,initial,greens,house):
        super().__init__(initial)
        self.greens = greens
        self.house = house
    def successor(self, state):

        successors = dict()
        pos, goal,house_dir=state
        for actions , (dx,dy) in dirs.items():
            nx=pos[0]+dx
            ny=pos[1]+dy
            if not(0<=nx<5 and 0<=ny<9):
                continue
            new_goal=goal
            new_dir = house_dir
            if 0 <= (goal[0] + house_dir) < 5:
                new_goal = (goal[0] + house_dir, goal[1])
            else:
                new_dir = -house_dir
                new_goal = (goal[0] + new_dir, goal[1])
            if not (nx,ny) in self.greens and (nx,ny) != new_goal:
                continue

            successors[actions] = ((nx, ny), new_goal, new_dir)
        return successors


    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        pos, goal, _ = state
        return pos == goal
    def h(self,node):
        pos,goal, _ = node.state
        return (abs(goal[0] - pos[0]) + abs(goal[1] - pos[1]))/5

if __name__ == "__main__":
    grid = (5,9)
    per = tuple(map(int,input().split(",")))
    house = tuple(map(int,input().split(",")))
    hDir = input()
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]

    initial = per, house, (1 if hDir == "right" else -1)
    problem = House(initial, allowed,hDir)
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())
