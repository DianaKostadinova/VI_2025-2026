from searching_framework import *

def toggle(state, x, y, n):
    board = [list(state[i*n:(i+1)*n]) for i in range(n)]
    for dx, dy in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] = 1 - board[nx][ny]
    return tuple(board[i][j] for i in range(n) for j in range(n))

class LightsOut(Problem):
    def __init__(self, initial, n):
        super().__init__(initial, goal=None)
        self.n = n

    def successor(self, state):
        successors = {}
        for i in range(self.n):
            for j in range(self.n):
                new_state = toggle(state, i, j, self.n)
                action = f"x: {i}, y: {j}"
                successors[action] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return all(c == 1 for c in state)

if __name__ == "__main__":
    n = int(input())
    fields = tuple(map(int, input().split(",")))
    problem = LightsOut(fields, n)
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())