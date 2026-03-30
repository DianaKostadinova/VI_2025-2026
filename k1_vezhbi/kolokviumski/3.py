from searching_framework import *

dir = {'Gore': (0, +1), 'Dolu': (0, -1), 'Desno': (+1, 0), 'Levo': (-1, 0), 'Stoj': (0, 0)}


class Lavirint(Problem):
    def __init__(self, initial_state, walls, goal=None, n=None, m=None):
        super().__init__(initial_state, goal)
        self.walls = walls
        self.n = n
        self.m = m

    def successor(self, state):
        successors = dict()
        x, y, timer, laserPos = state

        for action, (di, dj) in dir.items():
            nx, ny = x + di, y + dj
            ntimer = (timer % 4) + 1

            if ntimer == 1:
                nLaser = (x,y)
            else:
                nLaser = laserPos

            if ntimer == 4 and (nx == nLaser[0] or ny == nLaser[1]):
                continue
            if (nx, ny) in self.walls or not (0 <= nx < self.n and 0 <= ny < self.m):  # ← self.n, self.m
                continue

            successors[action] = (nx, ny, ntimer, nLaser)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        x, y, _, _ = state
        return (x, y) == self.goal


if __name__ == '__main__':
    read_two = lambda: tuple(map(int, input().split()))

    n, m = read_two()
    x, y = read_two()
    manPos = (x, y)
    x1, y2 = read_two()
    target = (x1, y2)
    timer = int(input())
    lx, ly = read_two()
    laser = (lx, ly)
    k = int(input())
    blocked = [read_two() for _ in range(k)]

    initial = (manPos[0], manPos[1], timer, laser)
    problem = Lavirint(initial, set(blocked), goal=target, n=n, m=m)
    solution = breadth_first_graph_search(problem)

    if solution is None:
        print("No solution")
    else:
        print(solution.solution())