import random
from deap import base, creator, tools
from modules.fitness import diet_fitness
from modules.config import chromosome_length


def setup_toolbox():
    # Remove previous creator classes if they exist (important in notebooks)
    if hasattr(creator, "FitnessMin"):
        delattr(creator, "FitnessMin")
    if hasattr(creator, "Individual"):
        delattr(creator, "Individual")

    # Create new fitness and individual classes for minimization problem
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    
    # Attribute generator: generates 0 or 1 randomly
    toolbox.register("attr_bool", lambda: random.randint(0, 1))
    # Individual generator: repeat attr_bool for chromosome length
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, chromosome_length)
    # Population generator: list of individuals
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    # Evaluation function (fitness)
    toolbox.register("evaluate", diet_fitness)
    # Crossover operator: two-point crossover
    toolbox.register("mate", tools.cxTwoPoint)
    # Mutation operator: flip bits with 5% chance per gene
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    # Selection operator: tournament selection with size 3
    toolbox.register("select", tools.selTournament, tournsize=3)

    return toolbox
