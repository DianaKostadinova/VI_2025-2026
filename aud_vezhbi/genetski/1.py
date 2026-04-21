import pygad

N = int(input())

def fitness_func(ga, solution, idx):
    return sum(solution)

params = {
    'num_generations': 500,
    'num_parents_mating': 20,
    'sol_per_pop': 50,
    'num_genes': N,

    'fitness_func': fitness_func,

    'gene_space': {'low': 0, 'high': 1},
    'gene_type': int,

    'mutation_type': 'random',
    'mutation_num_genes': 2
}

ga = pygad.GA(**params)
ga.run()

solution, _, _ = ga.best_solution()

print(solution)
print(sum(solution))