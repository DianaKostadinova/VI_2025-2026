import pygad


def read_input():
    M, N = map(int, input().split())
    K = int(input())
    B = int(input())

    unusable = set()
    for _ in range(B):
        r, c = map(int, input().split())
        unusable.add((r, c))

    return M, N, K, unusable


def get_watered_cells(r, c):
    cells = [
        (r, c),

        (r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
        (r, c - 1), (r, c + 1),
        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1),

        (r - 2, c),
        (r + 2, c),
        (r, c - 2),
        (r, c + 2)
    ]

    valid = set()

    for x, y in cells:
        if 0 <= x < M and 0 <= y < N and (x, y) not in unusable:
            valid.add((x, y))

    return valid


def fitness_func(ga_instance, solution, solution_idx):
    sprinklers = []
    watered = set()

    for i in range(0, len(solution), 2):
        r = solution[i]
        c = solution[i + 1]

        if (r, c) in unusable:
            continue

        sprinklers.append((r, c))

        covered = get_watered_cells(r, c)

        if (r, c) in covered:
            covered.remove((r, c))

        watered.update(covered)

    return len(watered) * 1000 - len(sprinklers)


if __name__ == "__main__":
    M, N, K, unusable = read_input()

    gene_space = []

    for _ in range(K):
        gene_space.append(range(M))
        gene_space.append(range(N))

    params = {
        'num_generations': 100,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': 2 * K,
        'gene_space': gene_space,
        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, _, _ = ga.best_solution()

    sprinklers = []
    watered = set()

    for i in range(0, len(best_solution), 2):
        r = best_solution[i]
        c = best_solution[i + 1]

        if (r, c) in unusable:
            continue

        if (r, c) not in sprinklers:
            sprinklers.append((r, c))

        covered = get_watered_cells(r, c)

        if (r, c) in covered:
            covered.remove((r, c))

        watered.update(covered)

    print(len(watered))
    print(len(sprinklers))

    for r, c in sprinklers:
        print(r, c)