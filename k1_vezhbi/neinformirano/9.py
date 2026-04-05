from searching_framework import Problem, breadth_first_graph_search


class Hanoi(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        n = len(state)
        for i in range(n):
            if not state[i]:
                continue
            top = state[i][-1]
            for j in range(n):
                if i == j:
                    continue
                if not state[j] or state[j][-1] > top:
                    new_state = list(state)
                    new_state[i] = new_state[i][:-1]
                    new_state[j] = new_state[j] + (top,)
                    action = f"MOVE TOP BLOCK FROM PILLAR {i} TO PILLAR {j}"
                    successors[action] = tuple(new_state)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == "__main__":
    full = open(0).read()
    start_str, goal_str = full.split(';;', 1)

    def parse_pillars(s):
        pillars = []
        for col in s.strip().split(';'):
            col = col.strip()
            if col:
                pillars.append(tuple(map(int, col.split(','))))
            else:
                pillars.append(())
        return tuple(pillars)

    initial = parse_pillars(start_str)
    goal    = parse_pillars(goal_str)

    problem  = Hanoi(initial, goal)
    solution = breadth_first_graph_search(problem)

    if solution is None:
        print("No Solution!")
    else:
        print(len(solution.solution()))
        for move in solution.solution():
            print(move)