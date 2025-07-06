import random
from deap import base, creator, tools
from modules.fitness import diet_fitness
from modules.config import chromosome_length

def setup_toolbox():
    if hasattr(creator, "FitnessMin"):
        delattr(creator, "FitnessMin")
    if hasattr(creator, "Individual"):
        delattr(creator, "Individual")

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("attr_bool", lambda: random.randint(0, 1))
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, chromosome_length)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("evaluate", diet_fitness)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    return toolbox
