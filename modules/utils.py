import random
import numpy as np
from modules.config import meal_df, target_nutrients
from modules.fitness import diet_fitness
from deap import creator

def evaluate_population(toolbox, population):
    invalid = [ind for ind in population if not ind.fitness.valid]
    fits = list(map(toolbox.evaluate, invalid))
    for ind, fit in zip(invalid, fits):
        ind.fitness.values = fit

def evaluate_population_parallel(toolbox, population):
    invalid = [ind for ind in population if not ind.fitness.valid]
    if not invalid:
        return
    fits = toolbox.map(toolbox.evaluate, invalid)
    for ind, fit in zip(invalid, fits):
        ind.fitness.values = fit

def local_search(individual, n_steps=10):
    best = creator.Individual(individual)
    best_fit = diet_fitness(best)[0]

    for _ in range(n_steps):
        neighbor = creator.Individual(best)
        i = random.randint(0, len(neighbor) - 1)
        neighbor[i] = 1 - neighbor[i]
        fit = diet_fitness(neighbor)[0]
        if fit < best_fit:
            best, best_fit = neighbor, fit
    return best

def print_best_solution(name, individual):
    nutrient_cols = ["Calories", "Protein", "Carbs", "Fat"]
    display_names = ["Calories", "Protein (g)", "Carbs (g)", "Fat (g)"]

    print(f"\n{name} Best Meal Plan:")

    selected_indices = [i for i, val in enumerate(individual) if val == 1]
    selected_meals = meal_df.iloc[selected_indices]

    print(f"{'Meal':<10} | {'Recipe Name':<65} | {'Cal':>5} | {'P':>3} | {'C':>3} | {'F':>3}")
    print("-" * 78)
    for _, row in selected_meals.iterrows():
        print(f"{row['Meal']:<10} | {row['RecipeName']:<65} | "
              f"{row['Calories']:5} | {row['Protein']:3} | {row['Carbs']:3} | {row['Fat']:3}")

    totals = selected_meals[nutrient_cols].sum()

    pct_of_total = totals / totals["Calories"] * 100
    pct_of_target = totals / target_nutrients * 100

    print("\nSummary (Totals and % of Targets):")
    print(f"{'Nutrient':<12} {'Total':>8} {'Target':>8} {'% of Total':>12} {'% of Target':>12}")
    print("-" * 56)

    for i, nutrient in enumerate(nutrient_cols):
        print(f"{display_names[i]:<12} "
              f"{totals[nutrient]:8.1f} "
              f"{target_nutrients[i]:8.1f} "
              f"{pct_of_total.iloc[i]:12.1f}% "
              f"{pct_of_target.iloc[i]:12.1f}%")

    fitness_val = diet_fitness(individual)[0]
    print(f"\nFitness: {fitness_val:.1f}")

def set_seeds(seed):
    random.seed(seed)
    np.random.seed(seed)
