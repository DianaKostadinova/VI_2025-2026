from searching_framework import *
dir = {"Up Left":(-2,+2), "Up Right":(+2,+2),"Down Left":(-2,-2), "Down Right":(+2,-2), "Left":(-2,0), "Right":(+2,0)}
class Check(Problem):
    def __init__(self, initial, size, walls, goal):
        super().__init__(initial, goal)
        self.size = size
        self.walls = set(walls)

    def successor(self, state):
        successors = dict()
        balls = set(state)

        for ball in balls:
            x, y = ball

            for action, (dx, dy) in dir.items():
                mid = (x + dx // 2, y + dy // 2)
                dest = (x + dx, y + dy)

                if not (0 <= dest[0] < self.size and 0 <= dest[1] < self.size):
                    continue

                if dest in self.walls:
                    continue

                if mid not in balls:
                    continue

                if dest in balls:
                    continue

                new_balls = set(balls)
                new_balls.remove(ball)
                new_balls.remove(mid)
                new_balls.add(dest)

                action_name = f"{action}: (x={x},y={y})"
                successors[action_name] = tuple(sorted(new_balls))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        if len(state) != 1:
            return False
        return state[0] == self.goal


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    balls = []
    for _ in range(m):
        balls.append(tuple(map(int, input().split(","))))

    wallNm = int(input())
    walls = []
    for _ in range(wallNm):
        walls.append(tuple(map(int, input().split(","))))

    goal = (n // 2, n - 1)

    initial = tuple(sorted(balls))

    problem = Check(initial, n, walls, goal)
    solution = breadth_first_graph_search(problem)

    if solution is None:
        print("No solution")
    else:
        print(solution.solution())