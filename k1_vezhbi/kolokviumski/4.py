from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    movies = dict()

    n = int(input())
    for _ in range(n):
        film_info = input()
        film, genre, time = film_info.split(' ')
        movies[film] = (float(time), genre)


    l_days = int(input())
    def no_overlap(start1,dur1,start2,dur2):
        return start1+dur1+1<=start2 or start2+dur2+1<=start1

    for movie in movies:
        time,genre = movies[movie]
        cinema_var = f"cinema_{movie}"
        problem.addVariable(cinema_var,[0,1])
        days_var = f"day_{movie}"
        problem.addVariable(days_var,range(1,l_days+1))
        hours_var = f"hours_{movie}"
        if genre.lower() == "horror":
            problem.addVariable(hours_var,range(21,24))
        else:
            problem.addVariable(hours_var,range(12,24))
    movie_list = list(movies.keys())
    for i in range(len(movie_list)):
        for j in range(i+1,len(movie_list)):
            m1 = movie_list[i]
            m2 = movie_list[j]
            time1,genre1 = movies[m1]
            time2,genre2 = movies[m2]

            if time1<2 and time2<2:
                problem.addConstraint(
                    lambda day1,day2: day1==day2, [f"day_{m1}", f"day_{m2}"]
                )
            problem.addConstraint(
                lambda d1,d2,c1,c2,s1,s2,dur1=time1,dur2=time2:
                ((c1!=c2) or (d1!=d2)) or
                 no_overlap(s1,dur1,s2,dur2),
                [f"day_{m1}",f"day_{m2}",f"cinema_{m1}",f"cinema_{m2}",f"hours_{m1}",f"hours_{m2}"]
            )
    result = problem.getSolution()
    if result:
        for movie in movies:
            print(
                f"{movie}: Day {result[f'day_{movie}']}  {result[f'hours_{movie}']}:00 - Cinema {result[f'cinema_{movie}']+1}")
    else:
        print("No Solution!")
