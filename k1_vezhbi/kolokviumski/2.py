from constraint import *
if __name__ == "__main__":
    problem = Problem(BacktrackingSolver())
    m = int(input())
    trees = []
    for i in range(m):
        trees.append(tuple(map(int, input().split())))
    domain = []
    for i in range(6):
        for j in range(6):
            if (i,j) not in trees:
                domain.append((i, j))
    for i in range(m):
        problem.addVariable(f"T{i}",domain)
    problem.addConstraint(AllDifferentConstraint(), [f"T{i}" for i in range(m)])
    def adj_tree(tent,tree):
        tx,ty = tent
        rx,ry = tree
        return (abs(tx-rx) == 1 and ty==ry) or (abs(ty-ry)==1 and tx==rx)

    for idx, tree in enumerate(trees):
        problem.addConstraint(lambda tent, t=tree: adj_tree(t, tent), [f"T{idx}"])

    def adj_tent(t1,t2):
        x1,y1 = t1
        x2,y2 = t2
        return abs(x1-x2) >= 1 or abs(y1-y2) >= 1


    tent_vars = [f"T{idx}" for idx in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            problem.addConstraint(adj_tent, (tent_vars[i], tent_vars[j]))
    solution = problem.getSolution()
    if solution:
        for t, pos in solution.items():
            print(f"{pos[0]} {pos[1]}")

