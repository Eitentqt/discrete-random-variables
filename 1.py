import random
import math
import matplotlib.pyplot as plt
import collections

p = float(input("Введите параметр p для геометрического распределения: "))
lambda_ = float(input("Введите параметр λ для распределения Пуассона: "))
n = int(input("Введите количество разыгранных значений: "))

def geometric_distribution(p):
    q = 1 - p
    m = 1
    U = random.uniform(0, 1)
    while U > p:
        U *= random.uniform(0, 1)
        m += 1
    return m

def poisson_distribution(lambda_):
    L = math.exp(-lambda_)
    m = 0
    P = 1
    while P > L:
        m += 1
        P *= random.uniform(0, 1)
    return m - 1

geom_samples = [geometric_distribution(p) for _ in range(n)]
poisson_samples = [poisson_distribution(lambda_) for _ in range(n)]

def generate_results(samples, title, filename):
    counter = collections.Counter(samples)
    keys = sorted(counter.keys())
    values = [counter[k] / n for k in keys]  
    
    with open(filename.replace(".png", ".txt"), "w") as f:
        f.write("Разыгранные значения | Количество разыгранных значений | Вероятность\n")
        for k, v in zip(keys, values):
            f.write(f"{k:<20} | {counter[k]:<30} | {v:.2f}\n")
    
    plt.figure()
    plt.bar(keys, values, width=0.6, alpha=0.7, edgecolor="black")
    plt.xlabel("Значение")
    plt.ylabel("Относительная частота")
    plt.title(title)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig(filename)
    plt.close()

generate_results(geom_samples, "Геометрическое распределение", "geometric_histogram.png")
generate_results(poisson_samples, "Распределение Пуассона", "poisson_histogram.png")
