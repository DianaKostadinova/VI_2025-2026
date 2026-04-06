from constraint import *
if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    movies = dict()
    for i in range(n):
        idx,genre,time = input().split()
        movies[idx] = (genre,float(time))
    nm_days = int(input())

    for movie in movies:
        genre,time = movies[movie]
        day_vars = f"day_{movie}"
        cinema_vars = f"cinema_{movie}"
        time_vars = f"time_{movie}"
        problem.addVariable(day_vars, range(1,nm_days+1))
        problem.addVariable(cinema_vars,[1,2])
        if genre == "children's":
            problem.addVariable(time_vars, range(12,19))
        else:
            problem.addVariable(time_vars, range(12,24))
    def overlap(s1,d1,s2,d2):
        return s1+d1+1<=s2 or s2+d2+1<=s1
    movie_list = list(movies.keys())
    for i in range(len(movie_list)):
        for j in range(i+1,len(movie_list)):
            m1 = movie_list[i]
            m2 = movie_list[j]
            genre1, time1 = movies[m1]
            genre2, time2 = movies[m2]
            problem.addConstraint(lambda s1,s2,c1,c2,d1,d2,dur1=time1, dur2=time2:
                                  ((c1!=c2) or (d1!=d2)) or overlap(s1,dur1,s2,dur2),
                                  [f"time_{m1}", f"time_{m2}", f"cinema_{m1}", f"cinema_{m2}", f"day_{m1}", f"day_{m2}"])
            if (genre1 == genre2) and genre1 in ["sci-fi", "horror", "action"] and  genre2 in ["sci-fi", "horror", "action"]:
                problem.addConstraint(
                    lambda c1,c2: c1==c2,[f"cinema_{m1}", f"cinema_{m2}"]
                )
    solution = problem.getSolution()
    if solution:
        for movie in movies:
           print( f"{movie}: Day {solution[f'day_{movie}']}  {solution[f'time_{movie}']}:00 - Cinema {solution[f'cinema_{movie}']}")
    else:
        print("No Solution!")