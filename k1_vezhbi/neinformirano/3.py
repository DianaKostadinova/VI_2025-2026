from searching_framework import *
dir = {"up":(0,+1), "down":(0,-1), "left":(-1,0), "right":(1,0)}
class Square(Problem):
    def __init__(self, initial,reden,goal=None):
        self.initial = initial
        self.reden = reden
        self.goal = goal
    def successor(self, state):
        successors = dict()
        x,y = state
        for action,(dx,dy) in dir.items():
            nx=x+dx
            ny=y+dy
            if 0<=nx<5 and 0<=ny<5:
                successors[f"Move square {self.reden+1} {action}"]=(nx, ny)
        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        x,y = state
        return (x,y) == self.goal
if __name__ == "__main__":
    grid = (5,5)
    squares = []
    for i in range(5):
        squares.append(tuple(map(int, input().split(","))))
    string_builder=[]
    for i in range(5):
        initial = (squares[i][0], squares[i][1])
        problem = Square(initial,i,(i,4-i))
        solution = breadth_first_graph_search(problem)
        if solution is None:
            string_builder = "No solution!"
        elif not solution.solution():
            continue
        else:
            string_builder+=solution.solution()

    print(string_builder)
