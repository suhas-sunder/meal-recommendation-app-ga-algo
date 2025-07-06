import pandas as pd
import numpy as np
import random
import time

# Prompt user to input daily calorie target (can override in notebooks if desired)
calories_target = float(input("Enter calorie limit (e.g. 2000): "))

# Randomly generate nutrient targets for protein, carbs, fat within reasonable ranges
protein_target = random.uniform(120, 180)
carbs_target = random.uniform(200, 300)
fat_target = random.uniform(50, 90)

# Meal type constraints: max allowed per meal type
meal_limits = {
    "Breakfast": 1,
    "Entrée": 2,
    "Protein": 2,
    "Side": 1,
    "Soup": 1
}

# Load meals and nutrition data from CSV relative to script location
meal_df = pd.read_csv("./data/Recipes.csv")

# Columns representing nutrient info
nutrient_columns = ["Calories", "Protein", "Carbs", "Fat"]

# Convert nutrient columns to numpy array for fast calculations
nutrient_data = meal_df[nutrient_columns].to_numpy()

# Target nutrients array for easy comparison in fitness function
target_nutrients = np.array([calories_target, protein_target, carbs_target, fat_target])

# Chromosome length = total number of meals (one gene per meal, 0 or 1)
chromosome_length = len(meal_df)

NUM_NUTRIENTS = len(target_nutrients)

# GA parameters
NGEN = 50
POP_SIZE = 100
CROSSOVER_PROB = 0.5
MUTATION_PROB = 0.2

# Timestamp seed for reproducibility/randomization
TIMESTAMP = int(time.time() * 1000) % 2**32

# Build mapping from meal type to indices in meal_df for meal count limits
meal_type_to_indices = {}
for i, meal_type in enumerate(meal_df["Meal"]):
    meal_type_to_indices.setdefault(meal_type, []).append(i)
