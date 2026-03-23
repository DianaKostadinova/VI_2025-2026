from searching_framework import *
dir = {"Gore": (0, +1), "Dolu": (0, -1), "Levo": (-1, 0), "Desno 2": (+2, 0), "Desno 3":(+3,0)}

class Player(Problem):
    def __init__(self, initial_state, border, walls,goal=None):
        super().__init__(initial_state,goal)
        self.border = border
        self.walls = walls
    def successor(self, state):
        successors=dict()
        (x,y)= state
        for action, (dx, dy) in dir.items():
            nx, ny = x + dx, y + dy
            if not (0 <= nx < self.border and 0 <= ny < self.border):
                continue
            blocked = False
            steps = max(abs(dx), abs(dy))
            step_x = dx // steps if dx != 0 else 0
            step_y = dy // steps if dy != 0 else 0
            for s in range(1, steps + 1):
                if (x + step_x * s, y + step_y * s) in self.walls:
                    blocked = True
                    break
            if not blocked:
                successors[action] = (nx, ny)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
      return state == self.goal
    def h(self,node):
        (x,y)=node.state
        (gx,gy)=self.goal
        return abs(x-gx)+abs(y-gy)

if __name__ == "__main__":
    borderSize = int(input().strip())
    numWalls = int(input().strip())
    walls = []
    for i in range(numWalls):
        walls.append(tuple(map(int, input().strip().split(","))))
    manPos = tuple(map(int, input().strip().split(",")))
    goalPos = tuple(map(int, input().strip().split(",")))

    player = Player(manPos, borderSize, walls, goalPos)
    result = astar_search(player)
    if result is None:
        print("No Solution!")
    else:
        print(result.solution())


