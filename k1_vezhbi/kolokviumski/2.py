from constraint import *

if __name__ == '__main__':
    n = 6
    m = int(input())
    trees = [tuple(map(int, input().split())) for _ in range(m)]

    domain = []
    for x in range(1, n):
        for y in range(1, n):
            if (x, y) not in trees:
                domain.append((x, y))

    problem = Problem()
    problem.addVariables(range(m), domain)
    problem.addConstraint(AllDifferentConstraint())

    def not_adjacent(t1, t2):
        return max(abs(t1[0] - t2[0]), abs(t1[1] - t2[1])) > 1

    for i in range(m):
        for j in range(i+1, m):
            problem.addConstraint(not_adjacent, (i, j))

    solution = problem.getSolution()

    if solution is None:
        print("No solution")
    else:
        for i in sorted(solution):
            print(f"{solution[i][0]} {solution[i][1]}")