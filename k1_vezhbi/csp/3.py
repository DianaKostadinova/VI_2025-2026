from constraint import *

if __name__ == "__main__":
    solver = input().strip()

    if solver == "BacktrackingSolver":
        solver1 = BacktrackingSolver()
    elif solver == "RecursiveBacktrackingSolver":
        solver1 = RecursiveBacktrackingSolver()
    elif solver == "MinConflictsSolver":
        solver1 = MinConflictsSolver()
    else:
        solver1 = BacktrackingSolver()
    problem = Problem(solver1)
    for i in range(81):
        problem.addVariable(i,range(1,10))
    for r in range(9):
        row = []
        for c in range(9):
            row.append(r*9+c)
        problem.addConstraint(AllDifferentConstraint(), row)
    for c in range(9):
        col = []
        for r in range(9):
            col.append(r*9+c)
        problem.addConstraint(AllDifferentConstraint(),col)
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            block = []
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    block.append(r * 9 + c)
            problem.addConstraint(AllDifferentConstraint(), block)
    print(problem.getSolution())
