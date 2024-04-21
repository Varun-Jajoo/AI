import math
import random
from math import sin

def f1(x):
    return -x**2

def f2(x):
    return sin(x)

def f3(x):
    return -(5*x**2) + (3*x) + 2

def best_neighbour(f, x, step=0.1):
    if f(x - step) > f(x):
        return x - step
    elif f(x + step) > f(x):
        return x + step
    else:
        return x

def hill_climbing(f, x, max_iterations=1000):
    for _ in range(max_iterations):
        neighbour = best_neighbour(f, x)
        if f(neighbour) > f(x):
            x = neighbour
        else:
            break
    return x

def main():
    ranges = [(-1, 1), (-math.pi, math.pi), (-100, 100)]
    functions = [f1, f2, f3]
    for i, f in enumerate(functions):
        x = random.uniform(*ranges[i])
        best_position = hill_climbing(f, x)
        print(f"For function {i+1}, the best position found is {best_position} with a value of {f(best_position)}.")

if __name__ == "__main__":
    main()
