from searching_framework import *
dir = {"up": (0,+1), "down": (0,-1), "left": (-1,0), "right": (1,0)}

class Person(Problem):
    def __init__(self, initial, goal=(4,4)):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        successors = dict()
        personPos, box1, box2 = state
        goal = self.goal

        for action_name, (dx,dy) in dir.items():
            new_px = personPos[0] + dx
            new_py = personPos[1] + dy

            if not (0 <= new_px < 5 and 0 <= new_py < 5):
                continue

            new_person = (new_px, new_py)
            newb1, newb2 = box1, box2

            if new_person == box1:
                pushed = (box1[0]+dx, box1[1]+dy)
                if (0 <= pushed[0] < 5 and 0 <= pushed[1] < 5) and (pushed != box2 or pushed == goal):
                    newb1 = pushed
                    action_full = f"Push box 1 {action_name}"
                else:
                    continue
            elif new_person == box2:
                pushed = (box2[0]+dx, box2[1]+dy)
                if (0 <= pushed[0] < 5 and 0 <= pushed[1] < 5) and (pushed != box1 or pushed == goal):
                    newb2 = pushed
                    action_full = f"Push box 2 {action_name}"
                else:
                    continue
            else:
                action_full = f"Move man {action_name}"

            successors[action_full] = (new_person, newb1, newb2)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        _, box1, box2 = state
        goal = self.goal
        return box1 == goal and box2 == goal
if __name__ == "__main__":
    grid = (5,5)
    personPos = tuple(map(int,input().split(",")))
    box1 = tuple(map(int,input().split(",")))
    box2 = tuple(map(int,input().split(",")))
    initial = (personPos, box1, box2)
    problem = Person(initial , goal=(4,4))
    solution = breadth_first_graph_search(problem)
    if solution is None:
        print("No Solution!")
    else:
        print(solution.solution())