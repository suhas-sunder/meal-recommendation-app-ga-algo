import random
import multiprocessing
import time
from deap import tools
from modules.toolbox import setup_toolbox
from modules.utils import evaluate_population, evaluate_population_parallel, local_search, set_seeds
from modules.config import POP_SIZE, NGEN, CROSSOVER_PROB, MUTATION_PROB, TIMESTAMP

def run_ga(memetic=False, parallel=True):
    set_seeds(TIMESTAMP)
    toolbox = setup_toolbox()

    if parallel:
        pool = multiprocessing.Pool()
        toolbox.register("map", pool.map)
    else:
        toolbox.register("map", map)

    pop = toolbox.population(n=POP_SIZE)

    if parallel:
        evaluate_population_parallel(toolbox, pop)
    else:
        evaluate_population(toolbox, pop)

    best_per_gen = []
    all_fitness = []

    for gen in range(NGEN):
        if gen % 10 == 0 or gen == NGEN-1:
            print(f"Generation {gen+1}/{NGEN} (memetic={memetic}, parallel={parallel})")

        fitness_vals = [ind.fitness.values[0] for ind in pop]
        all_fitness.append(fitness_vals)
        best = tools.selBest(pop, 1)[0]
        best_per_gen.append(best.fitness.values[0])

        offspring = list(map(toolbox.clone, toolbox.select(pop, len(pop))))

        for i in range(1, len(offspring), 2):
            if random.random() < CROSSOVER_PROB:
                toolbox.mate(offspring[i-1], offspring[i])
                del offspring[i-1].fitness.values
                del offspring[i].fitness.values

        for i in range(len(offspring)):
            if random.random() < MUTATION_PROB:
                toolbox.mutate(offspring[i])
                del offspring[i].fitness.values

            if memetic:
                offspring[i][:] = local_search(offspring[i])

        if parallel:
            evaluate_population_parallel(toolbox, offspring)
        else:
            evaluate_population(toolbox, offspring)

        pop[:] = offspring

    if parallel:
        pool.close()
        pool.join()

    best = tools.selBest(pop, 1)[0]
    return best_per_gen, best, all_fitness
