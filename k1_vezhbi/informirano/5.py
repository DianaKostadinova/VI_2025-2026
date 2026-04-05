from searching_framework import *

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
dir_names = ["up", "right", "down", "left"]

def move_snake(snake, direction, grow=False):
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    if grow:
        return tuple([new_head] + list(snake))
    else:
        return tuple([new_head] + list(snake[:-1]))

def heuristic(state):
    snake, apples, _ = state
    head = snake[0]
    if not apples:
        return 0
    return min(abs(head[0] - ax) + abs(head[1] - ay) for (ax, ay) in apples)

class SnakeProblem(Problem):
    def __init__(self, initial, apples, board_size=(10, 10), initial_dir=1):
        super().__init__((tuple(initial), tuple(apples), initial_dir))
        self.board_size = board_size

    def successor(self, state):
        snake, apples, dir_idx = state
        successors = {}

        for action_name, new_dir_idx in [("Move forward", dir_idx),
                                          ("Turn left", (dir_idx - 1) % 4),
                                          ("Turn right", (dir_idx + 1) % 4)]:
            dx, dy = dirs[new_dir_idx]
            new_head = (snake[0][0] + dx, snake[0][1] + dy)
            grow = new_head in apples
            if self.is_valid(new_head, snake, grow):
                new_snake = move_snake(snake, (dx, dy), grow)
                new_apples = tuple(a for a in apples if a != new_head)
                successors[action_name] = (new_snake, new_apples, new_dir_idx)

        return successors

    def is_valid(self, pos, snake, grow=False):
        x, y = pos
        if not (0 <= x < self.board_size[0] and 0 <= y < self.board_size[1]):
            return False
        body = snake if grow else snake[:-1]
        return pos not in body

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        _, apples, _ = state
        return len(apples) == 0

    def h(self, node):
        return heuristic(node.state)


if __name__ == "__main__":
    n_apples = int(input())
    apples = [tuple(map(int, input().split(','))) for _ in range(n_apples)]

    snake_start = ((5, 5), (5, 4), (5, 3))
    dir_start = 1

    problem = SnakeProblem(snake_start, apples, board_size=(10, 10), initial_dir=dir_start)
    solution = astar_search(problem, problem.h)

    if solution is None:
        print("No solution!")
    else:
        print(solution.solution())