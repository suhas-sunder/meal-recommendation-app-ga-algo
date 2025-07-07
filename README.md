---

## title: Meal Recommendation GA App

# Meal Recommendation App using Genetic Algorithm

This project applies Genetic Algorithms (GAs) to generate optimized daily meal plans based on nutritional targets such as calories, protein, carbohydrates, and fat. It was developed as part of a university project for exploring the difference between Basic GA, Parallel GA, and Memetic GA.

> **This project is based on:**
> “Optimization using Genetic Algorithm in Food Composition” [\[1\]](#1)
> “Towards Automatically Generating Meal Plan Based on Genetic Algorithm” [\[2\]](#2)
> Reference GitHub Repository: [AngelsGills/Meal-Recommendation-Optimization](https://github.com/AngelsGills/Meal-Recommendation-Optimization)
> **This Repository:** [suhas-sunder/meal-recommendation-app-ga-algo](https://github.com/suhas-sunder/meal-recommendation-app-ga-algo)

## Features

* Nutrient-based meal optimization using Genetic Algorithms
* Memetic variant with local search (hill climbing)
* Support for parallel evaluation (multiprocessing)
* Constraint handling on meal types (e.g., max 2 entrees, 1 breakfast)
* Visualizations of fitness over generations and distribution
* Runs on Jupyter Notebook with Python backend

## Setup Instructions (for all platforms)

> The project supports two versions:
>
> * **Default version**: Works on Linux (preferred)
> * **Windows/Mac version**: See `windows-mac-version/` folder

### 📦 Step-by-step Installation and Execution

All steps below can be executed inside a **Jupyter Notebook**.

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
# There can sometimes be issues with multiprocessing on those platforms because of the way the code is written.
# The code in `windows-mac-version/` is more stable and should work for those platforms because it uses the `threading` module and not `multiprocessing`. It also uses a delay timer to simulate additional compute time instead of actually adding computationally heavy loads.
```

## Input Data

* The dataset `Recipes@.csv` is loaded for all GA variants.
* This CSV file was sourced from the [reference GitHub repository](https://github.com/AngelsGills/Meal-Recommendation-Optimization).

## Outputs

* Optimized daily meal plan printed to the console
* Runtime comparison table
* Line plots for best fitness across generations
* Boxplots showing population fitness distribution

## Citation & References

<a id="1">\[1]</a> Adriyendi and Y. Melia, “Optimization using genetic algorithm in food composition,” *Research Gate*, vol. 1, no. 2, pp. 1–15, doi:10.12785/ijcds/100191. \[Online]. Available: [https://www.researchgate.net/publication/357234565\_Optimization\_using\_Genetic\_Algorithm\_in\_Food\_Composition](https://www.researchgate.net/publication/357234565_Optimization_using_Genetic_Algorithm_in_Food_Composition) *(accessed Jul. 1, 2025)*.

<a id="2">\[2]</a> N. Jia, J. Chen, R. Wang, and M. Li, “Towards automatically generating meal plan based on genetic algorithm,” *Soft Computing*, vol. 28, no. 9–10, pp. 6893–6908, Jan. 2024, doi:10.1007/s00500-023-09556-0. \[Online]. Available: [https://link.springer.com/article/10.1007/s00500-023-09556-0](https://link.springer.com/article/10.1007/s00500-023-09556-0) *(accessed Jul. 1, 2025)*.

---

## Notes

* Run instructions assume Jupyter Notebook environment.
* For any multiprocessing issues, disable parallel mode or use the alternate folder.
* Feedback and contributions are welcome!
