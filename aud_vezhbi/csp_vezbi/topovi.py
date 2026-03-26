from constraint import *

def notAttacking(cannon1,cannon2):
    row1,col1=cannon1
    row2,col2=cannon2
    return row1!=row2 and col1!=col2

if __name__ == '__main__':
    problem = Problem(MinConflictsSolver())
    variable = ["cannon_" + str(i) for i in range(8)]
    domain = [(row,col) for row in range(8) for col in range(8)]

    problem.addVariables(variable,domain)

    for cannon1 in variable:
        for cannon2 in variable:
            if cannon1 != cannon2:
                problem.addConstraint(notAttacking, (cannon1,cannon2))
    res = problem.getSolution()
    print(res)

    for row in range(8):
        for col in range(8):
            print("T" if (row, col) in res.values() else "_", end="")
        print()
