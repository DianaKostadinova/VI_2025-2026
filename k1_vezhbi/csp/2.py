from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(0,100))))
    problem.addConstraint(AllDifferentConstraint(),variables)
    problem.addConstraint(lambda a,b,c: a + b + c >= 100, ["A", "B", "C"])

    problem.addConstraint(lambda b:b%2==1, ["B"])
    problem.addConstraint(lambda d:d%2==1, ["D"])
    problem.addConstraint(lambda e:e%2==1, ["E"])


    problem.addConstraint(ExactSumConstraint(150), ["D","E"])

    problem.addConstraint(lambda f: f%10 in [0,4,8], ["F"])

    print(problem.getSolution())
