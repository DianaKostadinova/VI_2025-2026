from constraint import *

def notEqualColors(color1, color2):
    return color1 != color2
if __name__ == '__main__':
 problem = Problem()
 variable = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
 problem.addVariables(variable, ["R","G","B"])
 pairs = [("WA", "NT"), ("WA", "SA"), ("SA", "NT"), ("SA", "NSW"), ("SA", "Q"), ("SA", "V"), ("NT", "Q"), ("Q", "NSW"), ("NSW", "V")]
 for pair in pairs:
     problem.addConstraint(notEqualColors, pair)
 print(problem.getSolutions())
 print(problem.getSolution())
 res_iter = problem.getSolutionIter()
 for i in range(5):
     print(next(res_iter))