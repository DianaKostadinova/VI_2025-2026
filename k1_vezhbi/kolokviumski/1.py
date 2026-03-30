from searching_framework import *

dir = {'Gore': (1, 0), 'Desno': (0, 1)}

class Boxes(Problem):
    def __init__(self, initial, boxes, goal=None):
        super().__init__(initial, goal)
        self.boxes = set(boxes)

    def successor(self, state):
        successors = {}
        i, j, filled = state

        for action, (di, dj) in dir.items():
            ni, nj = i + di, j + dj

            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if (ni, nj) in self.boxes:
                continue

            new_filled = set(filled)

            for ddi in [-1, 0, 1]:
                for ddj in [-1, 0, 1]:
                    if ddi == 0 and ddj == 0:
                        continue
                    neighbor = (ni + ddi, nj + ddj)
                    if neighbor in self.boxes and neighbor not in new_filled:
                        new_filled.add(neighbor)

            successors[action] = (ni, nj, frozenset(new_filled))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        _, _, filled = state
        return len(filled) == len(self.boxes)


if __name__ == '__main__':
    n = int(input())
    man_pos = (n-1, 0)

    num_boxes = int(input())
    boxes = []

    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(','))))

    initial = (man_pos[0], man_pos[1], frozenset())

    problem = Boxes(initial, boxes)

    solution = breadth_first_graph_search(problem)

    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())