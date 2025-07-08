import random
import multiprocessing
import time
from deap import tools
from modules.toolbox import setup_toolbox
from modules.utils import evaluate_population, evaluate_population_parallel, local_search, set_seeds
from modules.config import POP_SIZE, NGEN, CROSSOVER_PROB, MUTATION_PROB, TIMESTAMP
from concurrent.futures import ThreadPoolExecutor

def run_ga(memetic=False, parallel=True):
    """
    Runs the Genetic Algorithm.
    
    Parameters:
    - memetic: whether to apply local search on offspring (memetic GA)
    - parallel: whether to evaluate fitness in parallel
    
    Returns:
    - best_per_gen: list of best fitness per generation
    - best: best individual found
    - all_fitness: list of fitness values for the entire population per generation
    """
    set_seeds(TIMESTAMP)  # Fix random seeds for reproducibility
    
    toolbox = setup_toolbox()  # Setup GA operators and structures
    
    # Register parallel or sequential map function for evaluation
    def thread_map(func, iterable):
        with ThreadPoolExecutor() as executor:
            return list(executor.map(func, iterable))
    
    if parallel:
        toolbox.register("map", thread_map)
    else:
        toolbox.register("map", map)

    
    # Initialize population
    pop = toolbox.population(n=POP_SIZE)
    
    # Evaluate initial population fitness
    if parallel:
        evaluate_population_parallel(toolbox, pop)
    else:
        evaluate_population(toolbox, pop)
    
    best_per_gen = []
    all_fitness = []
    
    # Evolution loop
    for gen in range(NGEN):
        if gen % 10 == 0 or gen == NGEN - 1:
            print(f"Generation {gen+1}/{NGEN} (memetic={memetic}, parallel={parallel})")
        
        # Record fitness values of current population
        fitness_vals = [ind.fitness.values[0] for ind in pop]
        all_fitness.append(fitness_vals)
        best = tools.selBest(pop, 1)[0]
        best_per_gen.append(best.fitness.values[0])
        
        # Select offspring
        offspring = list(map(toolbox.clone, toolbox.select(pop, len(pop))))
        
        # Apply crossover
        for i in range(1, len(offspring), 2):
            if random.random() < CROSSOVER_PROB:
                toolbox.mate(offspring[i-1], offspring[i])
                del offspring[i-1].fitness.values
                del offspring[i].fitness.values
        
        # Apply mutation and local search (if memetic)
        for i in range(len(offspring)):
            if random.random() < MUTATION_PROB:
                toolbox.mutate(offspring[i])
                del offspring[i].fitness.values
            
            if memetic:
                offspring[i][:] = local_search(offspring[i])
        
        # Evaluate offspring fitness
        if parallel:
            evaluate_population_parallel(toolbox, offspring)
        else:
            evaluate_population(toolbox, offspring)
        
        # Replace population with offspring
        pop[:] = offspring
    
    
    # Return best individual info
    best = tools.selBest(pop, 1)[0]
    return best_per_gen, best, all_fitness
