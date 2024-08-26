import sys
import random
class Population:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.population = self.makePopulation()

    def fitness(self, params: list) -> float:
        """Oblicza wartość funkcji przystosowania dla zestawu parametrów."""
        x = params[0]
        y = params[1]
        foo_value = (x - y) ** 2 + ((x + y - 10) / 3) ** 2
        return 1 / (foo_value)  if foo_value != 0 else 999999 # Odwrócenie wartości, aby zminimalizować funkcję

    def makePopulation(self) -> list:
        population = []
        for params in self.chromosome.chromosome:
            fitness_value = self.fitness(params)
            population.append((params, fitness_value))
        return population

    def best_Selection(self) -> list:
        # Select the top 10 individuals based on fitness values
        parents = [ind[0] for ind in sorted(self.population, key=lambda x: x[1], reverse=True)[:10]]
        return parents
    
    def how_Many_Groups(self) -> int:
        groups = int(input("How many groups in the tournament? "))
        # check
        if len(self.population) % groups != 0:
            raise ValueError("Population size must be divisible by the number of groups")
        return groups


    def tournament(self, groups : int) -> list:
        size_Groups = len(self.population) // groups
        random.shuffle(self.population) 
        parents = []
    
        for i in range(groups):
            group_Start = i * size_Groups
            group_End = group_Start + size_Groups
            group_Participants = self.population[group_Start : group_End]
            
            winner = max(group_Participants, key=lambda x: x[1])
            parents.append(winner[0])
        
        return parents
    
    def roulette(self) -> list:
        suma = sum(value[1] for value in self.population)
        pp = 0
        distributor = []
        parents = []
        for x in self.population:          
            pp += x[1]/suma
            distributor.append((x[0], pp))
        
        for _ in range(10):
            spin = random.uniform(0,1)
            for d in distributor:
                if (d[1] >= spin):
                    parents.append(d[0])
                    break
        return parents

    def evolve(self, groups_Amount: int, selection_Method: str, crossOver_Method: str, mutation_Method: str, mutation_Probability: float) -> None:
    # Selection phase
        if selection_Method == 'Best Selection':
            parents = self.best_Selection()
        
        elif selection_Method == 'Tournament Selection':
            parents = self.tournament(groups_Amount)

        elif selection_Method == 'Roulette Selection':
            parents = self.roulette()

        else:
            print("Wrong selection method specified.")
            exit(0)
        
        # Crossover and mutation phase handled by the chromosome's multiplication method
        new_Generation = self.chromosome.multiplication(parents, crossOver_Method, mutation_Method, mutation_Probability)
        
        # Evaluate the new population
        self.population = [(x, self.fitness(x)) for x in new_Generation]


    def best_solution(self, i: int, best_solutions: list) -> list:
        # Find the individual with the best fitness in the current population
        best_solution = max(self.population, key=lambda x: x[1])
        best_solutions.append(best_solution)

        # Display the best solution for this generation
        print(f"Generation {i} best solution:")
        params = best_solution[0]  # The parameters (e.g., [x, y])
        fitness_value = best_solution[1]
        print(f"Parameters: {params}")
        print(f"Fitness: {fitness_value}")
        
        # Optionally, stop the algorithm if the fitness is good enough
        if fitness_value > 1e6:  # Adjust this threshold based on your problem
            self.print_best(best_solutions)
            sys.exit()
        
        return best_solutions

    def print_best(self, best_solutions: list) -> None:
        # Find the best solution across all generations
        best_solution = max(best_solutions, key=lambda x: x[1])
        
        print("Best solution found:")
        params = best_solution[0]  # The parameters (e.g., [x, y])
        fitness_value = best_solution[1]
        
        # Display the parameters and corresponding fitness
        formatted_params = ', '.join([f'{param:.6f}' for param in params])
        print(f"Parameters: [{formatted_params}]")
        
        # Convert the fitness value to its corresponding objective function value
        objective_value = 1 / fitness_value if fitness_value != 0 else float('inf')
        
        # Display the value in decimal format
        print(f"Value: {objective_value:.20f}")
