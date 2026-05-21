import pygad
import random
random.seed(0)

rooms = {
    1: {'name': 'Modern & Contemporary Art', 'adjacent': [2, 7], 'value': 110},
    2: {'name': 'European History', 'adjacent': [1, 3, 4, 5, 7], 'value': 130},
    3: {'name': 'Seasonal Exhibitions', 'adjacent': [2], 'value': 100},
    4: {'name': 'Prehistory', 'adjacent': [2, 6, 10], 'value': 140},
    5: {'name': 'Medieval Times', 'adjacent': [2, 6, 9], 'value': 120},
    6: {'name': 'Arms and Armor', 'adjacent': [4, 5], 'value': 150},
    7: {'name': 'Arts of Africa, Oceania and the Americas', 'adjacent': [1, 2, 8], 'value': 90},
    8: {'name': 'Greek and Roman History', 'adjacent': [7, 9], 'value': 180},
    9: {'name': 'The Great Hall', 'adjacent': [5, 8, 10], 'value': 30},
    10: {'name': 'Egyptian History', 'adjacent': [4, 9], 'value': 200}
}

K = int(input())

large_rooms = {2, 8, 9, 10}
def fitness_func(ga, solution, idx):
    camera_count = {room_id:0 for room_id in rooms}
    for gene in solution:
        room_id = int(gene)
        camera_count[room_id] += 1
    coverage = {room_id: 0 for room_id in rooms}
    for room_id in rooms:
        count = camera_count[room_id]
        if count == 0:
            continue
        if room_id in large_rooms:
            coverage[room_id] = 1.0 if count >=2 else 0.6
        else:
            coverage[room_id] = 1.0
    for room_id in rooms:
        count = camera_count[room_id]
        if count == 0:
            continue
        for adj in rooms[room_id]['adjacent']:
            coverage[adj] =min(coverage[adj], coverage[room_id])
    total_value = sum(coverage[room_id] * rooms[room_id]['value'] for room_id in rooms)
    return total_value


params = {
     'num_generations': 1000,
    'sol_per_pop': 100,
    'num_parents_mating': 40,
    'num_genes': K,
    'gene_space': list(range(1, 11)),
    'gene_type': int,
    'fitness_func': fitness_func,
    'mutation_num_genes': 1,
    'random_state': 0
}

ga = pygad.GA(**params)

ga.run()

best_solution, _, _ = ga.best_solution()
best_fitness = fitness_func(None, best_solution, 0)

print(f'Optimal protected value: {best_fitness}M$')
