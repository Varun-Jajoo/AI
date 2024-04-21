import random


# Step 1: Determine the number of chromosomes, generation, mutation rate, and crossover rate value
def genetic_algorithm(num_chromosomes, mutation_rate, crossover_rate, num_variables):
    # Step 2: Generate chromosome population with random initialization
    population = generate_population(num_chromosomes, num_variables)

    i = int(1)

    while True:

        # Step 3: Evaluation of fitness value of chromosomes
        fitness_values = [fitness_function(chromosome) for chromosome in population]

        # Step 8: Solution (Best Chromosomes)
        best_chromosome = population[fitness_values.index(min(fitness_values))]

        # print(f"Generation {i}: solution: {best_chromosome}, Fitness: {min(fitness_values)}")

        if min(fitness_values) == 0:
            print(f"\nGeneration {i}: Best solution: {best_chromosome}, Fitness: {min(fitness_values)}")
            print(f"Optimal Solution after {i} Generations")
            break
        i = i + 1
        next_generation = []

        # Step 5: Chromosomes selection
        selected_population = selection(population, fitness_values)

        for _ in range(num_chromosomes // 2):
            parent1, parent2 = selected_population[random.randint(0, len(selected_population) - 1)], \
                               selected_population[random.randint(0, len(selected_population) - 1)]

            # Step 6: Crossover
            child1, child2 = crossover(parent1, parent2, crossover_rate)

            # Step 7: Mutation
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)

            next_generation.extend([child1, child2])

        population = next_generation

    return best_chromosome


# Step 2: Generate initial population
def generate_population(size, num_variables):
    population = []
    for _ in range(size):
        individual = [random.randint(0, 10) for _ in range(num_variables)]
        population.append(individual)
    return population


# Step 4: Fitness function evaluation
def fitness_function(variables):
    a, b, c, d = variables
    return abs((a + 2 * b + 3 * c + 4 * d) - 30)


# Step 5: Chromosome selection using roulette wheel selection
def selection(population, fitness_values):
    selected_population = []
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]

    for _ in range(len(population)):
        selected = random.choices(population, probabilities)[0]
        selected_population.append(selected)

    return selected_population


# Step 6: Crossover
def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2
    return parent1, parent2


# Step 7: Mutation
def mutation(individual, mutation_rate):
    if random.random() < mutation_rate:
        index = random.randint(0, len(individual) - 1)
        new_value = random.randint(0, 10)
        individual[index] = new_value
    return individual


def get_input():
    num_chromosomes = int(input("Enter the number of chromosomes: "))

    mutation_rate = float(input("Enter the mutation rate: "))
    crossover_rate = float(input("Enter the crossover rate: "))
    num_variables = 4  # Assuming 4 variables (a,b,c,d) for the given equation
    return num_chromosomes, mutation_rate, crossover_rate, num_variables


def main():
    num_chromosomes, mutation_rate, crossover_rate, num_variables = get_input()
    best_chromosome = genetic_algorithm(num_chromosomes, mutation_rate, crossover_rate, num_variables)
    print("Best solution:", best_chromosome)


if __name__ == "__main__":
    main()
