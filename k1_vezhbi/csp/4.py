from constraint import *
from math import factorial

def n_queens_solver(n):
    if n <= 0:
        return

    solver = BacktrackingSolver()
    problem = Problem(solver)

    variables = ["Q{}".format(i) for i in range(n)]
    problem.addVariables(variables, range(n))

    for i in range(n):
        for j in range(i + 1, n):
            problem.addConstraint(
                lambda r1, r2, c1=i, c2=j: r1 != r2 and abs(r1 - r2) != abs(c1 - c2),
                ("Q{}".format(i), "Q{}".format(j))
            )

    if n <= 6:
        solutions = problem.getSolutions()
        if not solutions:
            print(0)
            return
        print(len(solutions) * factorial(n))
    else:
        solution = problem.getSolution()
        if solution is None:
            print(n)
            return
        result = {}
        for col in range(n):
            row = solution["Q{}".format(col)]
            result[col + 1] = (row, col)
        print(result)

if __name__ == "__main__":
    n = int(input())
    n_queens_solver(n)
