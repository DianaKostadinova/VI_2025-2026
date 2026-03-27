from constraint import *

if __name__ == '__main__':

    bands = dict()
    order = []

    band_info = input()
    while band_info != 'end':
        band, genre, time = band_info.split()
        bands[band] = (genre, time)
        order.append(band)
        band_info = input()

    variables = list(bands.keys())
    domain = ['S1', 'S2', 'S3']

    problem = Problem()

    problem.addVariables(variables, domain)

    def constraint_func(*args):
        assignment = dict(zip(variables, args))
        for stage in domain:
            durations = [int(bands[b][1]) for b in variables if assignment[b] == stage]
            if durations.count(120) > 1:
                return False
            if len([d for d in durations if d < 80]) > 5:
                return False
        return True

    problem.addConstraint(constraint_func, variables)

    genres = {}
    for band, (genre, time) in bands.items():
        genres.setdefault(genre, []).append(band)

    for genre, band_list in genres.items():
        total_time = sum(int(bands[b][1]) for b in band_list)
        if total_time <= 300:
            problem.addConstraint(AllEqualConstraint(), band_list)

    result = problem.getSolution()

    if result:
        for band in order:
            print(f"{band} ({bands[band]}): {result[band]}")