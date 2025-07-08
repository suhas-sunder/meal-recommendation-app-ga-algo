---
title: Meal Recommendation GA App
---

# Meal Recommendation App using Genetic Algorithm

This project applies Genetic Algorithms (GAs) to generate optimized daily meal plans based on nutritional targets such as calories, protein, carbohydrates, and fat. It was developed as part of a university project for exploring the difference between Basic GA, Parallel GA, and Memetic GA.

> **This project is based on:**
> “Optimization using Genetic Algorithm in Food Composition” [\[1\]](#1)  
> “Towards Automatically Generating Meal Plan Based on Genetic Algorithm” [\[2\]](#2)  
> Reference GitHub Repository: [AngelsGills/Meal-Recommendation-Optimization](https://github.com/AngelsGills/Meal-Recommendation-Optimization)  
> **This Repository:** [suhas-sunder/meal-recommendation-app-ga-algo](https://github.com/suhas-sunder/meal-recommendation-app-ga-algo)

## Features

- Nutrient-based meal optimization using Genetic Algorithms  
- Memetic variant with local search (hill climbing)  
- Support for parallel evaluation (multiprocessing)  
- Constraint handling on meal types (e.g., max 2 entrees, 1 breakfast)  
- Visualizations of fitness over generations and distribution  
- Runs on Jupyter Notebook with Python backend  

## Setup Instructions (for all platforms)

> The project supports two versions:
>
> - **Default version**: Works on Linux (preferred)  
> - **Windows/Mac version**: See `windows-mac-version/` folder  

### 📦 Step-by-step Installation and Execution

All steps below can be executed inside a **Jupyter Notebook**:

```bash
# 1. Clone the repository
!git clone https://github.com/suhas-sunder/meal-recommendation-app-ga-algo.git

# 2. Change into the directory
%cd meal-recommendation-app-ga-algo

# 3. Open and run setup-install.ipynb
#    This installs all required Python packages using pip.

# 4. Run main.py or open the notebook version to execute the algorithm
#    main.py includes all runs: Basic, Parallel, and Memetic GA

# NOTE: If you are on Windows or Mac and the parallel version fails,
# run the code inside the `windows-mac-version/` folder instead.
# The code in that folder avoids multiprocessing issues on those platforms.
