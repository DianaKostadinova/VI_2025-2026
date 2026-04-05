
from searching_framework import *
dirs = {"Up": (0,+1), "Down": (0,-1), "Left": (-1,0), "Right": (1,0)}

class Robot(Problem):
    def __init__(self, initial, walls,goal=None):
        super().__init__(initial, goal)
        self.walls = walls
    def successor(self, state):
        successors = dict()
        robotPos, tools = state
        x, y = robotPos
        for actions, (dx, dy) in dirs.items():
            nx, ny = x + dx, y + dy
            if not (0<=nx<10 and 0<=ny<10):
                continue
            if (nx,ny) in self.walls:
                continue
            newTools = tuple(t for t in tools if t != (nx, ny))
            if (nx, ny) in [M1_pos, M2_pos]:
                successors["Repair"] = ((nx, ny), newTools)
            else:
                successors[actions] = ((nx, ny), newTools)
        return successors
    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        (x,y),tools = state
        return (x,y) == self.goal and len(tools)==0

if __name__ == '__main__':
    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())
    parts_M1 = int(input())
    to_collect_M1 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M1)])
    parts_M2 = int(input())
    to_collect_M2 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M2)])

    walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5), (1, 6), (1, 7), (0, 6), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9)]
    all_tools = tuple(to_collect_M1+to_collect_M2)
    final=M2_pos
    initial_state = (robot_start_pos, all_tools)
    problem = Robot(initial_state, walls, final)

    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())