from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))
    problem.addConstraint(AllDifferentConstraint(),variables)



    def crypt_constraint(S, E,N,D,M,O,R,Y):
        send = 1000 * S + 100 * E + 10 * N + D
        more = 1000 * M + 100 * O + 10 * R + E
        money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

        return send + more == money


    problem.addConstraint(
        crypt_constraint,
        variables
    )

    print(problem.getSolution())