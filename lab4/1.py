import pygad
import math

N, M, R = map(float, input().split())
N = int(N)
M = int(M)

points = [tuple(map(float, input().split())) for _ in range(N)]

def decode(solution):
    umbrellas = []

    for i in range(M):
        x = int(solution[i*3])
        y = int(solution[i*3+1])
        active = int(solution[i*3+2])

        if active == 1:
            umbrellas.append((x, y))

    return umbrellas


def fitness_func(ga, solution, idx):
    umbrellas = decode(solution)
    penalty = 0

    # uncovered points
    uncovered = 0
    for px, py in points:
        ok = False
        for ux, uy in umbrellas:
            if math.dist((px, py), (ux, uy)) < R:
                ok = True
                break
        if not ok:
            uncovered += 1

    if uncovered > 0:
        penalty += uncovered * 100000

    # overlaps
    for i in range(len(umbrellas)):
        for j in range(i+1, len(umbrellas)):
            d = math.dist(umbrellas[i], umbrellas[j])

            if d < 8 * R / 5:
                penalty += 1000
            elif d <= 2 * R:
                penalty += 100

    # number of umbrellas
    penalty += len(umbrellas) * 10

    return -penalty


# SAME PRINCIPLE AS YOUR WORKING TASK
gene_space = []

for _ in range(M):
    gene_space += [
        list(range(0, 11)),  # x
        list(range(0, 11)),  # y
        [0, 1]               # active
    ]


params = {
    'num_generations': 300,
    'sol_per_pop': 80,
    'num_parents_mating': 20,

    'num_genes': 3 * M,
    'gene_space': gene_space,

    'fitness_func': fitness_func,

    'mutation_num_genes': 1,
    'save_best_solutions': True
}

ga = pygad.GA(**params)
ga.run()

solution, _, _ = ga.best_solution()
fitness = fitness_func(None, solution, 0)
best_solutions = ga.best_solutions

print(solution)
print(fitness)