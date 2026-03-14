from searching_framework import Problem, breadth_first_graph_search

dir = {"Up": (0, +1), "Down": (0, -1), "Left": (-1, 0), "Right": (+1, 0)}

class Robot(Problem):
    def __init__(self, initial, M1_pos, M1_steps, M2_pos, M2_steps, to_collect_M1, to_collect_M2, walls, goal=None):
        super().__init__(initial, goal)
        self.M1_pos = M1_pos
        self.M1_steps = M1_steps
        self.M2_pos = M2_pos
        self.M2_steps = M2_steps
        self.to_collect_M1 = to_collect_M1
        self.to_collect_M2 = to_collect_M2
        self.walls = set(walls)

    def successor(self, state):
        successors = dict()
        (x, y), collected_M1, repaired_M1, collected_M2, repaired_M2, repair_count = state

        # Movement
        for action, (dx, dy) in dir.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in self.walls:
                successors[action] = ((nx, ny), collected_M1, repaired_M1, collected_M2, repaired_M2, 0)

        # Repair actions
        if not repaired_M1 and (x, y) == self.M1_pos and len(collected_M1) == len(self.to_collect_M1):
            if repair_count + 1 == self.M1_steps:
                successors['Repair'] = ((x, y), collected_M1, True, collected_M2, repaired_M2, 0)
            else:
                successors['Repair'] = ((x, y), collected_M1, repaired_M1, collected_M2, repaired_M2, repair_count + 1)

        elif repaired_M1 and not repaired_M2 and (x, y) == self.M2_pos and len(collected_M2) == len(self.to_collect_M2):
            if repair_count + 1 == self.M2_steps:
                successors['Repair'] = ((x, y), collected_M1, repaired_M1, collected_M2, True, 0)
            else:
                successors['Repair'] = ((x, y), collected_M1, repaired_M1, collected_M2, repaired_M2, repair_count + 1)

        # Collect parts
        new_collected_M1 = collected_M1
        new_collected_M2 = collected_M2
        if not repaired_M1 and (x, y) in self.to_collect_M1 and (x, y) not in collected_M1:
            new_collected_M1 = collected_M1 + ((x, y),)
        if repaired_M1 and not repaired_M2 and (x, y) in self.to_collect_M2 and (x, y) not in collected_M2:
            new_collected_M2 = collected_M2 + ((x, y),)

        # Update successors with collected parts
        for key in list(successors.keys()):
            s = successors[key]
            successors[key] = (s[0], new_collected_M1, s[2], new_collected_M2, s[4], s[5])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[2] and state[4]  # repaired_M1 and repaired_M2

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

    initial_state = (robot_start_pos, (), False, (), False, 0)
    problem = Robot(initial_state, M1_pos, M1_steps, M2_pos, M2_steps, to_collect_M1, to_collect_M2, walls)

    result = breadth_first_graph_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")