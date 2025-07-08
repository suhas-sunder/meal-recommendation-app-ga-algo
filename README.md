---
title: Meal Recommendation GA App
---

# Meal Recommendation App using Genetic Algorithm

This project applies Genetic Algorithms (GAs) to generate optimized daily meal plans based on nutritional targets such as calories, protein, carbohydrates, and fat. It was developed as part of a university project for exploring the difference between Basic GA, Parallel GA, and Memetic GA.

> **This project is based on:**
> “Optimization using Genetic Algorithm in Food Composition” [\[4\]](#4)  
> “Towards Automatically Generating Meal Plan Based on Genetic Algorithm” [\[5\]](#5)  
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

```

[1] T. O. Ting, X.-S. Yang, S. Cheng, and K. Huang, “Hybrid Metaheuristic Algorithms: Past, Present, and Future,” Studies in Computational Intelligence, pp. 71–83, Dec. 2014, doi: https://doi.org/10.1007/978-3-319-13826-8_4.

[2] J. Jumana and H. a. A. Al-Zubaidi, “Optimizing IoT wireless Sensor Networks: A comparative analysis of particle swarm Optimization (PSO) and Genetic Algorithms (GA),” Fusion Practice and Applications, vol. 15, no. 2, pp. 278–287, Jan. 2024, doi: 10.54216/fpa.150223.

[3] E.-G. Talbi, Metaheuristics: From Design to Implementation. Hoboken, NJ, USA: Wiley Publishing, 2009.

[4] Adriyendi and Y. Melia, “Optimization using genetic algorithm in food composition,”  Research Gate, vol. 1, no. 2, pp. 1-15, doi:10.12785/ijcds/100191. [Online]. https://www.researchgate.net/publication/357234565_Optimization_using_Genetic_Algorithm_in_Food_Composition (accessed Jul. 1, 2025). 

[5] N. Jia, J. Chen, R. Wang, and M. Li, “Towards automatically generating meal plan based on genetic algorithm,” Soft Computing, vol. 28, no. 9–10, pp. 6893–6908, Jan. 2024, doi: 10.1007/s00500-023-09556-0. [Online]. https://link.springer.com/article/10.1007/s00500-023-09556-0 (accessed Jul. 1, 2025).
