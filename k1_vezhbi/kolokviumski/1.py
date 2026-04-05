from searching_framework import *

dirs = {"Gore": (0, +1), "Desno": (+1, 0)}
arr = [(1,0),(1,1),(-1,0),(-1,1),(0,-1),(0,1),(-1,-1),(1,-1)]

class Boxes(Problem):
    def __init__(self, initial, grid_size, box):
        super().__init__(initial)
        self.grid_size = grid_size
        self.box = box

    def successor(self, state):
        successors = dict()
        person_pos, nm_boxes, box_frozen = state
        box = dict(box_frozen)

        for action, (dx, dy) in dirs.items():
            nx = person_pos[0] + dx
            ny = person_pos[1] + dy
            if not (0 <= nx < self.grid_size[0] and 0 <= ny < self.grid_size[1]):
                continue
            if (nx, ny) in box:
                continue
            newBox = dict(box)
            newNm = nm_boxes
            for (ax, ay) in arr:
                adj = (nx + ax, ny + ay)
                if adj in newBox and not newBox[adj]:
                    newBox[adj] = True
                    newNm -= 1
                    break
            successors[action] = (nx, ny), newNm, frozenset(newBox.items())

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        _, nm, _ = state
        return nm == 0


if __name__ == '__main__':
    n = int(input())
    grid = (n, n)
    nm_boxes = int(input())
    boxes = {}
    for _ in range(nm_boxes):
        pos = tuple(map(int, input().split(",")))
        boxes[pos] = False

    person_pos = (0, 0)
    boxes_frozen = frozenset(boxes.items())
    initial = person_pos, nm_boxes, boxes_frozen
    problem = Boxes(initial, grid, boxes)
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())