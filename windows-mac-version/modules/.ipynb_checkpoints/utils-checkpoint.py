import random
import numpy as np
from modules.config import meal_df, target_nutrients
from modules.fitness import diet_fitness
from deap import creator
from IPython.display import display, HTML

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

    selected_indices = [i for i, val in enumerate(individual) if val == 1]
    selected_meals = meal_df.iloc[selected_indices]

    # --- Build meal table HTML ---
    html = f"<h3>{name} Best Meal Plan</h3>"
    html += "<table style='border-collapse: collapse; font-family: monospace;'>"
    html += "<tr><th style='padding:4px;text-align:left;'>Meal</th>" \
            "<th style='padding:4px;text-align:left;'>Recipe Name</th>" \
            "<th style='padding:4px;'>Cal</th>" \
            "<th style='padding:4px;'>P</th>" \
            "<th style='padding:4px;'>C</th>" \
            "<th style='padding:4px;'>F</th></tr>"

    for _, row in selected_meals.iterrows():
        html += f"<tr><td style='padding:4px;'>{row['Meal']}</td>" \
                f"<td style='padding:4px;'>{row['RecipeName']}</td>" \
                f"<td style='padding:4px;'>{row['Calories']}</td>" \
                f"<td style='padding:4px;'>{row['Protein']}</td>" \
                f"<td style='padding:4px;'>{row['Carbs']}</td>" \
                f"<td style='padding:4px;'>{row['Fat']}</td></tr>"

    html += "</table>"

    # --- Summary ---
    totals = selected_meals[nutrient_cols].sum()
    pct_of_total = totals / totals["Calories"] * 100
    pct_of_target = totals / target_nutrients * 100

    html += "<h4>Summary (Totals and % of Targets)</h4>"
    html += "<table style='border-collapse: collapse;'>"
    html += "<tr><th style='text-align:left;padding:4px;'>Nutrient</th>" \
            "<th style='padding:4px;'>Total</th>" \
            "<th style='padding:4px;'>Target</th>" \
            "<th style='padding:4px;'>% of Total</th>" \
            "<th style='padding:4px;'>% of Target</th></tr>"

    colors = ["blue", "green", "orange", "purple"]

    for i, nutrient in enumerate(nutrient_cols):
        html += f"<tr><td style='color:{colors[i]};padding:4px;'>{display_names[i]}</td>" \
                f"<td style='padding:4px;'>{totals[nutrient]:.1f}</td>" \
                f"<td style='padding:4px;'>{target_nutrients[i]:.1f}</td>" \
                f"<td style='padding:4px;'>{pct_of_total.iloc[i]:.1f}%</td>" \
                f"<td style='padding:4px;'>{pct_of_target.iloc[i]:.1f}%</td></tr>"

    html += "</table>"

    # --- Fitness value ---
    fitness_val = diet_fitness(individual)[0]
    html += f"<p><b>Fitness:</b> {fitness_val:.1f}</p>"

    display(HTML(html))

def set_seeds(seed):
    random.seed(seed)
    np.random.seed(seed)
