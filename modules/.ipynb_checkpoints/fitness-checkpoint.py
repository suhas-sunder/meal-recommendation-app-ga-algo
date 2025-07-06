import numpy as np
from modules.config import nutrient_data, target_nutrients, meal_limits, meal_type_to_indices

def diet_fitness(individual):
    _ = sum(i ** 2 for i in range(10000))  # ~1ms CPU work (simulate)
    selected = np.array(individual)
    totals = selected @ nutrient_data
    deviation = np.abs(totals - target_nutrients)
    penalty = 0
    for meal_type, max_allowed in meal_limits.items():
        indices = meal_type_to_indices.get(meal_type, [])
        count = sum(individual[i] for i in indices)
        if count > max_allowed:
            penalty += (count - max_allowed) * 100
    return (np.sum(deviation) + penalty,)
