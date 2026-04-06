from math import factorial

from constraint import *
if __name__ == "__main__":
    n = int(input())
    problem = Problem(BacktrackingSolver())
    for i in range(n):
        problem.addVariable(i,range(n))
    for i in range(n):
        for j in range(i+1,n):
            problem.addConstraint(
                lambda r1,r2,c1=i,c2=j: r1!=r2 and abs(r1-r2) != abs(c1-c2), (i,j)
            )
    if n<=6:
        solutions = problem.getSolutions()
        if not solutions:
            print(0)
        print(len(solutions) * factorial(n))
    else:
        solution = problem.getSolution()
        if solution is None:
            print(n)
        result = {}
        for col in range(n):
            row = solution[(col)]
            result[col + 1] = (row, col)
        print(result)