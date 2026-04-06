from constraint import *
if __name__ == '__main__':
    problem =Problem()
    problem.addVariable("Simona_attendance",[0,1])
    problem.addVariable("Marija_attendance",[0,1])
    problem.addVariable("Petar_attendance",[0,1])
    problem.addVariable("time_meeting",range(12,20))
    problem.addConstraint(lambda s: s==1,["Simona_attendance"])
    problem.addConstraint(lambda t,s: s==0 if t not in {13,14,16,19} else True,["time_meeting","Simona_attendance"])
    problem.addConstraint(lambda t,m: m==0 if t not in {14,15,18} else True,["time_meeting","Marija_attendance"])
    problem.addConstraint(lambda t,p: p==0 if t not in {12,13,16,17,18,19} else True,["time_meeting","Petar_attendance"])
    problem.addConstraint(lambda s,m,p:s==1 and (m+p)>=1, ["Simona_attendance", "Marija_attendance", "Petar_attendance"])
    solution = problem.getSolutions()
    for sol in solution:
        key_order = ["Simona_attendance","Marija_attendance","Petar_attendance","time_meeting"]
        sorted_sol = {k: sol[k] for k in key_order}
        print(sorted_sol)