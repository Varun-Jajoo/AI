import random

def binaryConversion(chromosome):
    return bin(chromosome)[2:].zfill(5)

def mutation(chromosome):
    mutationPoint = random.randint(0, 4)
    mutatedBit = 1 << mutationPoint
    mutatedChromosome = chromosome ^ mutatedBit

    return mutatedChromosome

def main():
    population = [random.randint(0, 15) for _ in range(6)]
    mutationRate = 0.5

    print("Before Mutation: ")
    for chromosome in population:
        print(f"{chromosome}: {binaryConversion(chromosome)}")

    for i in range(len(population)):
        if random.random() < mutationRate:
            population[i] = mutation(population[i])

    print("After Mutation: ")
    for chromosome in population:
        print(f"{chromosome}: {binaryConversion(chromosome)}")


if __name__ == '__main__':
    main()
