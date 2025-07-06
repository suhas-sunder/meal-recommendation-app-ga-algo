# visualizer.py

import matplotlib.pyplot as plt
import numpy as np

def plot_fitness(fitness_basic, fitness_parallel, fitness_memetic):
    """
    Plot the fitness of the different GA variants over generations.
    """
    plt.figure(figsize=(10, 6))

    # Line plots with markers
    plt.plot(fitness_basic, label='Basic GA', marker='s', markersize=3)
    plt.plot(fitness_parallel, label='Parallel GA', marker='s', markersize=3)
    plt.plot(fitness_memetic, label='Memetic GA', marker='s', markersize=3)

    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("GA Variants Fitness Comparison")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Annotated points
    n = len(fitness_basic)
    idx_basic = int(n * 0.10)
    idx_parallel = int(n * 0.20)
    idx_memetic = int(n * 0.30)

    plt.annotate(f"Basic GA: {fitness_basic[idx_basic]:.4f}",
                 xy=(idx_basic, fitness_basic[idx_basic]),
                 xytext=(-30, 25), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->'), fontsize=8, color='blue')

    plt.annotate(f"Parallel GA: {fitness_parallel[idx_parallel]:.4f}",
                 xy=(idx_parallel, fitness_parallel[idx_parallel]),
                 xytext=(-30, 45), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->'), fontsize=8, color='orange')

    plt.annotate(f"Memetic GA: {fitness_memetic[idx_memetic]:.4f}",
                 xy=(idx_memetic, fitness_memetic[idx_memetic]),
                 xytext=(10, 40), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->'), fontsize=8, color='green')

    plt.show()

def plot_boxplots(all_basic, all_parallel, all_memetic, NGEN):
    """
    Create boxplots showing the distribution of fitness for each GA variant.
    """
    for ga_data, name, color in [
        (all_basic, 'Basic GA', 'C0'),
        (all_parallel, 'Parallel GA', 'C1'),
        (all_memetic, 'Memetic GA', 'C2')
    ]:
        plt.figure(figsize=(12, 6))
        plt.boxplot(
            ga_data,
            positions=range(1, NGEN + 1),
            widths=0.6,
            patch_artist=True,
            boxprops=dict(facecolor=color, alpha=0.5),
            medianprops=dict(color='black')
        )
        plt.xlabel("Generation")
        plt.ylabel("Fitness Distribution")
        plt.title(f"{name} Population Fitness Distribution Per Generation")
        plt.xticks(range(1, NGEN + 1))
        plt.grid(True)
        plt.tight_layout()
        plt.show()

def print_runtime_table(basic, parallel, memetic):
    """
    Prints a table summarizing the runtime and speed changes between different GA variants.
    """
    def pct_speedup(base, other):
        return (1 - other / base) * 100

    print("\nGA Variant Runtime Summary:")
    print(f"{'Variant':<15}{'Time (s)':>10}{'Speed Change':>30}")
    print("-" * 45)

    print(f"{'Basic GA':<15}{basic:10.2f}{'Baseline':>30}")

    parallel_diff = pct_speedup(basic, parallel)
    print(f"{'Parallel GA':<15}{parallel:10.2f}{abs(parallel_diff):19.1f}% {'faster' if parallel_diff > 0 else 'slower'}")

    memetic_diff = pct_speedup(basic, memetic)
    memetic_label = f"{abs(memetic_diff):.1f}% {'faster' if memetic_diff > 0 else 'slower'}"
    print(f"{'Memetic GA':<15}{memetic:10.2f}{memetic_label:>20}")
