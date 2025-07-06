import pandas as pd
import numpy as np
import random
import time

# Input from user when main runs (you can override in notebook if needed)
calories_target = float(input("Enter calorie limit (e.g. 2000): "))

protein_target = random.uniform(120, 180)
carbs_target = random.uniform(200, 300)
fat_target = random.uniform(50, 90)

meal_limits = {
    "Breakfast": 1,
    "Entrée": 2,
    "Protein": 2,
    "Side": 1,
    "Soup": 1
}

# Adjust path relative to modules/
meal_df = pd.read_csv("./data/Recipes.csv")
nutrient_columns = ["Calories", "Protein", "Carbs", "Fat"]
nutrient_data = meal_df[nutrient_columns].to_numpy()
target_nutrients = np.array([calories_target, protein_target, carbs_target, fat_target])
chromosome_length = len(meal_df)

NUM_NUTRIENTS = len(target_nutrients)
NGEN = 50
POP_SIZE = 100
CROSSOVER_PROB = 0.5
MUTATION_PROB = 0.2
TIMESTAMP = int(time.time() * 1000) % 2**32

# Build dictionary: meal_type to list of indices
meal_type_to_indices = {}
for i, meal_type in enumerate(meal_df["Meal"]):
    meal_type_to_indices.setdefault(meal_type, []).append(i)
