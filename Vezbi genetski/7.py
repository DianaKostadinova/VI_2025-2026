import pygad
import numpy as np


def fitness_func(ga_instance, solution, solution_idx):
    preferred_type = solution[0]

    machines = []

    for i in range(N):
        machines.append((i, repair_times[i], machine_types[i]))

    order = solution[1:]

    used = set()
    arranged = []

    for x in order:
        if x not in used:
            arranged.append(machines[x])
            used.add(x)

    total_time = 0

    for i in range(0, N, 4):
        team = arranged[i:i + 4]

        times = [x[1] for x in team]
        types = [x[2] for x in team]

        # special rule
        if all(t == preferred_type for t in types):
            total_time += min(times)
        else:
            total_time += max(times)

    # pygad maximizes fitness
    return -total_time


if __name__ == '__main__':

    N = int(input())

    repair_times = []
    machine_types = []

    all_types = set()

    for _ in range(N):
        t, c = input().split()
        t = int(t)

        repair_times.append(t)
        machine_types.append(c)

        all_types.add(c)

    all_types = list(all_types)

    # gene 0 -> preferred type index
    # other genes -> permutation of machines

    gene_space = []

    gene_space.append(range(len(all_types)))

    for _ in range(N):
        gene_space.append(range(N))

    params = {
        'num_generations': 300,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': N + 1,
        'gene_space': gene_space,
        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }

    ga = pygad.GA(**params)

    ga.run()

    best_solution, _, _ = ga.best_solution()

    preferred_type = all_types[best_solution[0]]

    machines = []

    for i in range(N):
        machines.append((i, repair_times[i], machine_types[i]))

    order = best_solution[1:]

    used = set()
    arranged = []

    for x in order:
        if x not in used:
            arranged.append(machines[x])
            used.add(x)

    total_time = 0
    teams = []

    for i in range(0, N, 4):
        team = arranged[i:i + 4]

        teams.append(team)

        times = [x[1] for x in team]
        types = [x[2] for x in team]

        if all(t == preferred_type for t in types):
            total_time += min(times)
        else:
            total_time += max(times)

    print(total_time)
    print(preferred_type)

    for idx, team in enumerate(teams):
        print(f"Team {idx + 1}:")

        for machine in team:
            print(machine[0], machine[1], machine[2])