import random

# Constants
length_of_population = 10
total_number_of_population = 10
mutation_rate = 0.1  # Mutation probability

# Generate a random population
def generate_population():
    return [random.choice([0, 1]) for _ in range(length_of_population)]

# Calculate fitness value (sum of 1s in the population)
def check_fitness_value(population):
    return sum(population)

# Perform crossover between two populations
def crossover_population(parent1, parent2):
    crossover_point = random.randint(1, length_of_population - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutate a population based on mutation rate
def mutate_population(population, mutation_rate):
    for i in range(len(population)):
        if random.random() < mutation_rate:
            population[i] = 1 - population[i]  # Flip bit
    return population

# Main genetic algorithm
def genetic_algorithm():
    total_population = [generate_population() for _ in range(total_number_of_population)]
    iteration_number = 0
    max_fitness = length_of_population  # Max possible fitness value
    
    while True:
        fitness_values = [check_fitness_value(individual) for individual in total_population]
        max_value = max(fitness_values)
        
        print(f"Iteration no: {iteration_number}, Max fitness value: {max_value}")
        
        # Stop condition: If max fitness value is reached
        if max_value == max_fitness:
            print(total_population)
            print("Optimal solution found!")
            break
        
        # Selection: Sort population by fitness (descending) and pick top half
        sorted_population = [x for _, x in sorted(zip(fitness_values, total_population), reverse=True)]
        top_half = sorted_population[:total_number_of_population // 2]
        
        # Crossover: Create next generation
        next_generation = []
        while len(next_generation) < total_number_of_population:
            parent1, parent2 = random.sample(top_half, 2)
            child1, child2 = crossover_population(parent1, parent2)
            next_generation.extend([child1, child2])
        
        # Mutation
        total_population = [mutate_population(ind, mutation_rate) for ind in next_generation]
        
        iteration_number += 1

# Run the genetic algorithm
genetic_algorithm()
