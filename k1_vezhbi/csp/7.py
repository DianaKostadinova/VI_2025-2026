from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lecture_slots_AI = int(input())
    lecture_slots_ML = int(input())
    lecture_slots_R = int(input())
    lecture_slots_BI = int(input())

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_12", "Fri_13", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15",
                         "Wed_10", "Wed_11", "Wed_12", "Wed_13", "Wed_14", "Wed_15",
                         "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_exercises_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    AI_vars = [f"AI_lecture_{i + 1}" for i in range(lecture_slots_AI)]
    ML_vars = [f"ML_lecture_{i + 1}" for i in range(lecture_slots_ML)]
    R_vars = [f"R_lecture_{i + 1}" for i in range(lecture_slots_R)]
    BI_vars = [f"BI_lecture_{i + 1}" for i in range(lecture_slots_BI)]

    if lecture_slots_AI > 0:
        AI_lab = "AI_exercises"
        problem.addVariable(AI_lab, AI_exercises_domain)
    if lecture_slots_ML > 0:
        ML_lab = "ML_exercises"
        problem.addVariable(ML_lab, ML_exercises_domain)
    if lecture_slots_BI > 0:
        BI_lab = "BI_exercises"
        problem.addVariable(BI_lab, BI_exercises_domain)

    for var in AI_vars:
        problem.addVariable(var, AI_lectures_domain)
    for var in ML_vars:
        problem.addVariable(var, ML_lectures_domain)
    for var in R_vars:
        problem.addVariable(var, R_lectures_domain)
    for var in BI_vars:
        problem.addVariable(var, BI_lectures_domain)

    all_vars = AI_vars + ML_vars + R_vars + BI_vars
    if lecture_slots_AI > 0:
        all_vars.append(AI_lab)
    if lecture_slots_ML > 0:
        all_vars.append(ML_lab)
    if lecture_slots_BI > 0:
        all_vars.append(BI_lab)

    problem.addConstraint(AllDifferentConstraint(), all_vars)

    if lecture_slots_ML > 0:
        for lec in ML_vars:
            problem.addConstraint(lambda l, lab: l != lab, (lec, ML_lab))

    solution = problem.getSolution()

    print(solution)