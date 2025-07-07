import numpy as np
from modules.config import nutrient_data, target_nutrients, meal_limits, meal_type_to_indices
import time

def diet_fitness(individual):
    # Simulate some CPU work (~1 ms) to make fitness evaluation realistic
    #_ = sum(i ** 2 for i in range(10000))
    time.sleep(0.0002)  # sleep for 10 milliseconds

    # Convert individual (list of 0/1) to numpy array for vectorized operations
    selected = np.array(individual)

    # Calculate total nutrients for selected meals: dot product
    totals = selected @ nutrient_data  # nutrient_data shape: (num_meals, num_nutrients)

    # Calculate absolute difference from target nutrients
    deviation = np.abs(totals - target_nutrients)

    # Penalty for violating meal limits (e.g., too many breakfasts)
    penalty = 0
    for meal_type, max_allowed in meal_limits.items():
        indices = meal_type_to_indices.get(meal_type, [])
        count = sum(individual[i] for i in indices)  # how many meals of this type are selected
        if count > max_allowed:
            # Add a big penalty for each extra meal of this type
            penalty += (count - max_allowed) * 100

    # Fitness value is total deviation plus penalty (we minimize this)
    return (np.sum(deviation) + penalty,)
