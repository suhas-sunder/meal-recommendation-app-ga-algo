import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display, HTML

def plot_fitness(fitness_basic, fitness_parallel, fitness_memetic):
    """
    Plot best fitness per generation for each GA variant.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(fitness_basic, label='Basic GA', marker='s', markersize=3)
    plt.plot(fitness_parallel, label='Parallel GA', marker='s', markersize=3)
    plt.plot(fitness_memetic, label='Memetic GA', marker='s', markersize=3)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("GA Variants Fitness Comparison")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

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
    Show boxplots of population fitness per generation for each GA variant.
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
    Print runtime summary with colors in Jupyter Notebook.
    """
    def pct_speedup(base, other):
        return (1 - other / base) * 100

    html = "<h4>GA Variant Runtime Summary:</h4>"
    html += "<table style='border-collapse: collapse;'>"
    html += "<tr><th style='text-align:left;padding:4px;'>Variant</th><th style='padding:4px;'>Time (s)</th><th style='padding:4px;'>Speed Change</th></tr>"
    html += "<tr><td style='color:blue;padding:4px;'>Basic GA</td><td style='padding:4px;'>{:.2f}</td><td style='padding:4px;'>Baseline</td></tr>".format(basic)

    parallel_diff = pct_speedup(basic, parallel)
    html += "<tr><td style='color:orange;padding:4px;'>Parallel GA</td><td style='padding:4px;'>{:.2f}</td><td style='padding:4px;'>{:.1f}% {}</td></tr>".format(
        parallel, abs(parallel_diff), "faster" if parallel_diff > 0 else "slower"
    )

    memetic_diff = pct_speedup(basic, memetic)
    html += "<tr><td style='color:green;padding:4px;'>Memetic GA</td><td style='padding:4px;'>{:.2f}</td><td style='padding:4px;'>{:.1f}% {}</td></tr>".format(
        memetic, abs(memetic_diff), "faster" if memetic_diff > 0 else "slower"
    )

    html += "</table>"

    display(HTML(html))
