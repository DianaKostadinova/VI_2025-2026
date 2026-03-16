from searching_framework import *

dir = {"up": (0, +1), "down": (0, -1), "right": (+1, 0), "up-right": (+1, +1), "down-right": (+1, -1)}
ball_dir = dir.copy()
def around_obstacle(pos_ball, obstacle):
    coordinates = [
        (2, 2), (3, 2), (4, 2),
        (2, 3), (2, 4),
        (4, 2), (4, 3), (4, 4),
        (3, 4), (4, 4),
        (4, 5), (5, 5), (6, 5),
        (5, 3), (6, 3)
    ]
    if pos_ball in coordinates:
        return True

class Player(Problem):
    def __init__(self, initial_state, goalBlock, player1, player2, goal=None):
        super().__init__(initial_state, goal)
        self.player1 = player1
        self.player2 = player2
        self.goalBlock = goalBlock

    def ball_valid(self, ball):
        bx, by = ball
        for px, py in [self.player1, self.player2]:
            if abs(bx - px) <= 1 and abs(by - py) <= 1:
                return False
        return True

    def is_blocked(self, ball, obstacles):
        bx, by = ball
        for ox, oy in obstacles:
            if abs(bx - ox) <= 1 and abs(by - oy) <= 1:
                return True
        return False

    def successor(self, state):
        successors = dict()
        (x, y), ballx, bally, player1, player2 = state
        ball = (ballx, bally)
        obstacles = [player1, player2]  # can add more static obstacles

        for action_name, (dx, dy) in dir.items():
            nx, ny = x + dx, y + dy
            if (nx, ny) == ball:
                new_ball = (ballx + dx, bally + dy)
                if 0 <= new_ball[0] < 8 and 0 <= new_ball[1] < 6 and self.ball_valid(new_ball):
                    successors[f"Push ball {action_name}"] = ((nx, ny), new_ball[0], new_ball[1], player1, player2)

            elif (nx, ny) != player1 and (nx, ny) != player2 and not self.is_blocked(ball, obstacles):
                successors[f"Move man {action_name}"] = ((nx, ny), ballx, bally, player1, player2)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        ball = (state[1], state[2])
        return ball in self.goalBlock

if __name__ == '__main__':
    player1 = (5,4)
    player2 = (3,3)
    goalBlock = ((7,2),(7,3))
    man_pos = tuple(map(int, input().split(",")))
    ball_pos = tuple(map(int, input().split(",")))
    initial_state = (man_pos, ball_pos[0], ball_pos[1], player1, player2)
    problem = Player(initial_state, goalBlock, player1, player2)
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())